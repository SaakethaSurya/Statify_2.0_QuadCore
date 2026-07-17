import os
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.messages import ToolMessage

class StatifyMCPClientManager:
    def __init__(self):
        # Configuration setup targeting the vector-db SSE endpoint over the Docker network
        self.server_config = {
            "vector-db-server": {
                "url": "http://vector-db:8001/sse"
            }
        }
        self.client = None

    async def initialize(self):
        # FIX: We pass self.server_config directly without any 'server_configs=' keyword
        self.client = MultiServerMCPClient(self.server_config)

    async def execute_tool_safely(self, tool_name: str, tool_args: dict, message_id: str):
        """
        Executes an MCP server tool statelessly.
        Catches execution errors gracefully and pipes them straight back to the model 
        as a ToolMessage with status='error' to trigger agent self-correction.
        """
        try:
            result = await self.client.invoke_tool(tool_name, tool_args)
            return ToolMessage(content=str(result), tool_call_id=message_id, status="success")
        except Exception as e:
            error_msg = f"Execution Failure in {tool_name}: {str(e)}"
            return ToolMessage(content=error_msg, tool_call_id=message_id, status="error")

    async def close(self):
        if self.client:
            await self.client.close()