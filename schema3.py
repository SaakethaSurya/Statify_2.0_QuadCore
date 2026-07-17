from pydantic import BaseModel, Field

class AnalysisRequest(BaseModel):
    ticker: str = Field(..., description="The stock ticker symbol (e.g., RELIANCE, TCS)", example="RELIANCE")
    position_size_inr: float = Field(..., description="Simulated position size out of a 1,000,000 INR portfolio", example=150000.0)

class AnalysisResponse(BaseModel):
    ticker: str
    position_size_inr: str
    status: str
    trading_thesis: str