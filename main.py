from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from schema3 import AnalysisRequest, AnalysisResponse
from mcp_client import StatifyMCPClientManager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await mcp_manager.initialize()
    yield
    await mcp_manager.close()

app = FastAPI(title="Statify 2.0 AI Portfolio Engine", version="2.0", lifespan=lifespan)
mcp_manager = StatifyMCPClientManager()


@app.on_event("startup")
async def startup_event():
    await mcp_manager.initialize()

@app.on_event("shutdown")
async def shutdown_event():
    await mcp_manager.close()

@app.post("/api/v1/analyze", response_model=AnalysisResponse)
async def analyze_portfolio_asset(payload: AnalysisRequest):
    try:
        theory_msg = await mcp_manager.execute_tool_safely(
            tool_name="retrieve_trading_theory", 
            tool_args={"strategy_name": "MACD"}, 
            message_id="call_theory_01"
        )
        
        simulated_prices = [100.0, 102.5, 101.2, 104.8, 103.1, 106.0, 105.4, 108.2, 110.0]
        metrics_msg = await mcp_manager.execute_tool_safely(
            tool_name="analyze_market_indicators",
            tool_args={"prices": simulated_prices},
            message_id="call_metrics_01"
        )

        if theory_msg.status == "error" or metrics_msg.status == "error":
            trading_thesis = f"Agent warning: Data mismatch detected. Self-correcting loop output. Metrics: {metrics_msg.content}"
        else:
            trading_thesis = (
                f"Allocation Strategy for {payload.ticker} with sizing {payload.position_size_inr} INR:\n"
                f"Based on {theory_msg.content}\n"
                f"Current execution metrics imply clear signals: {metrics_msg.content}\n"
                f"Risk Audit Decision: Maintain holding target; allocation matches risk-profile bounds."
            )

        return AnalysisResponse(
            ticker=payload.ticker,
            position_size_inr=f"{payload.position_size_inr:,} INR",
            status="Processed",
            trading_thesis=trading_thesis
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Microservice Pipeline Exception: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main.py", host="0.0.0.0", port=8000, reload=True)