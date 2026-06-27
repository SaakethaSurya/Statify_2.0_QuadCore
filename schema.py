from pydantic import BaseModel

class StockInput(BaseModel):
    company: str

class NewsInput(BaseModel):
    company: str