import os
import asyncio
from mcp.server import Server
from mcp.server.sse import SseServerTransport
from starlette.applications import Starlette
from starlette.routing import Route
import uvicorn

from tools3 import calculate_sma, calculate_ema, calculate_macd

# Initialize a standard MCP Server
server = Server("Statify Quant Vector DB Engine")

TRADING_THEORIES = {
    "MACD": "Moving Average Convergence Divergence tracks momentum shifts using 12 and 26-period EMAs.",
    "SMA": "Simple Moving Average provides baseline support/resistance trends evenly weighted.",
    "EMA": "Exponential Moving Average reacts faster to recent price fluctuations over traditional SMAs."
}

# Register the tools with the server
@server.list_tools()
async def handle_list_tools():
    return [
        {
            "name": "retrieve_trading_theory",
            "description": "Retrieves theoretical quantitative context for a specific strategy (SMA, EMA, MACD).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "strategy_name": {"type": "string"}
                },
                "required": ["strategy_name"]
            }
        },
        {
            "name": "analyze_market_indicators",
            "description": "Executes structural calculations across SMA, EMA, and MACD indicators for analysis.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "prices": {
                        "type": "array",
                        "items": {"type": "number"}
                    }
                },
                "required": ["prices"]
            }
        }
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict):
    if name == "retrieve_trading_theory":
        strategy_name = arguments.get("strategy_name", "").upper()
        if strategy_name in TRADING_THEORIES:
            return [{"type": "text", "text": f"Context for {strategy_name}: {TRADING_THEORIES[strategy_name]}"}]
        raise ValueError(f"Strategy '{strategy_name}' not found.")
        
    elif name == "analyze_market_indicators":
        prices = arguments.get("prices", [])
        if not prices or len(prices) < 5:
            raise ValueError("Insufficient pricing data points.")
        
        sma_val = calculate_sma(prices)
        ema_val = calculate_ema(prices)
        macd_data = calculate_macd(prices)
        
        metrics_text = (
            f"Calculated Metrics Profile:\n"
            f"- 20-Day SMA: {sma_val:.2f}\n"
            f"- 12-Day EMA: {ema_val:.2f}\n"
            f"- MACD Line: {macd_data['macd']:.2f}, Signal Line: {macd_data['signal']:.2f}, Histogram: {macd_data['histogram']:.2f}"
        )
        return [{"type": "text", "text": metrics_text}]
        
    raise ValueError(f"Tool {name} not found.")

# Create the SSE transport layer for Docker networking
sse = SseServerTransport("/sse")

async def handle_sse(request):
    async with sse.connect_sse(request.scope, request.receive, request._send):
        await server.run(
            request.scope,
            request.receive,
            request._send,
            server.create_initialization_options()
        )

# Package it into a lightweight Starlette web application
app = Starlette(routes=[
    Route("/sse", endpoint=handle_sse, methods=["GET"]),
    Route("/message", endpoint=sse.handle_post_message, methods=["POST"])
])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)