"""
Stock related entity models
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class StockEntity(BaseModel):
    """Stock entity"""
    id: Optional[int] = None
    code: str = Field(..., description="Stock code")
    name: str = Field(..., description="Stock name")
    market: str = Field(..., description="Market type")
    price: float = Field(..., description="Current price")
    change_percent: float = Field(..., description="Price change percentage")
    volume: Optional[int] = Field(None, description="Volume")
    turnover: Optional[float] = Field(None, description="Turnover")
    market_cap: Optional[str] = Field(None, description="Market capitalization")
    pe_ratio: Optional[float] = Field(None, description="P/E ratio")
    pb_ratio: Optional[float] = Field(None, description="P/B ratio")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class StockAnalysisEntity(BaseModel):
    """Stock analysis entity"""
    id: Optional[int] = None
    stock_code: str = Field(..., description="Stock code")
    analysis_type: str = Field(..., description="Analysis type")
    technical_data: Optional[dict] = Field(None, description="Technical analysis data")
    fundamental_data: Optional[dict] = Field(None, description="Fundamental analysis data")
    risk_data: Optional[dict] = Field(None, description="Risk assessment data")
    recommendation: Optional[str] = Field(None, description="Investment recommendation")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
