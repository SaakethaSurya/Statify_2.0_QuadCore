from pydantic import BaseModel
from typing import List

class AgentState(BaseModel):
    ticker: str
    price: float = 0
    rsi: float = 0
    news: List[str] = []
    recommendation: str = ""
    needs_more_data: bool = False