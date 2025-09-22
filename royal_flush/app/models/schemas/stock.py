"""
Stock related data schemas
"""
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class MarketType(str, Enum):
    """Market type enumeration"""
    A_STOCK = "a_stock"
    HK_STOCK = "hk_stock"
    US_STOCK = "us_stock"

class AnalysisType(str, Enum):
    """Analysis type enumeration"""
    BASIC = "basic"
    TECHNICAL = "technical"
    FUNDAMENTAL = "fundamental"
    COMPREHENSIVE = "comprehensive"

class StockAnalysisRequest(BaseModel):
    """Stock analysis request"""
    stock_code: str = Field(..., description="Stock code", example="000001")
    market: MarketType = Field(..., description="Market type", example="a_stock")
    analysis_type: AnalysisType = Field(default=AnalysisType.BASIC, description="Analysis type")

class StockSearchRequest(BaseModel):
    """Stock search request"""
    query: str = Field(..., description="Search keyword", example="Ping An")
    market: MarketType = Field(..., description="Market type", example="a_stock")
    limit: int = Field(default=10, description="Return limit")

class StockInfo(BaseModel):
    """Stock basic information"""
    code: str = Field(..., description="Stock code")
    name: str = Field(..., description="Stock name")
    price: float = Field(..., description="Current price")
    change_percent: float = Field(..., description="Price change percentage")
    market_cap: Optional[str] = Field(None, description="Market capitalization")
    pe_ratio: Optional[float] = Field(None, description="P/E ratio")
    volume: Optional[int] = Field(None, description="Volume")
    turnover: Optional[float] = Field(None, description="Turnover")

class TechnicalAnalysis(BaseModel):
    """Technical analysis results"""
    rsi: float = Field(..., description="RSI indicator")
    macd: dict = Field(..., description="MACD indicator")
    bollinger_bands: dict = Field(..., description="Bollinger Bands")
    moving_averages: dict = Field(..., description="Moving averages")
    trend: str = Field(..., description="Trend")
    support_level: float = Field(..., description="Support level")
    resistance_level: float = Field(..., description="Resistance level")

class FundamentalAnalysis(BaseModel):
    """Fundamental analysis results"""
    pe_ratio: float = Field(..., description="P/E ratio")
    pb_ratio: float = Field(..., description="P/B ratio")
    roe: float = Field(..., description="ROE")
    debt_ratio: float = Field(..., description="Debt ratio")
    revenue_growth: float = Field(..., description="Revenue growth rate")
    profit_growth: float = Field(..., description="Profit growth rate")
    industry_rank: int = Field(..., description="Industry ranking")
    market_position: str = Field(..., description="Market position")

class RiskAssessment(BaseModel):
    """Risk assessment results"""
    risk_level: str = Field(..., description="Risk level")
    volatility: float = Field(..., description="Volatility")
    beta: float = Field(..., description="Beta coefficient")
    max_drawdown: float = Field(..., description="Max drawdown")
    var_95: float = Field(..., description="95% VaR")
    liquidity_risk: str = Field(..., description="Liquidity risk")
    credit_risk: str = Field(..., description="Credit risk")

class StockAnalysisResult(BaseModel):
    """Stock analysis results"""
    stock_info: StockInfo = Field(..., description="Stock basic information")
    technical_analysis: Optional[TechnicalAnalysis] = Field(None, description="Technical analysis")
    fundamental_analysis: Optional[FundamentalAnalysis] = Field(None, description="Fundamental analysis")
    risk_assessment: Optional[RiskAssessment] = Field(None, description="Risk assessment")
    recommendation: Optional[str] = Field(None, description="Investment recommendation")

class StockAnalysisResponse(BaseModel):
    """Stock analysis response"""
    success: bool = Field(..., description="Whether request succeeded")
    message: str = Field(..., description="Response message")
    data: Optional[StockAnalysisResult] = Field(None, description="Analysis result")
    timestamp: str = Field(..., description="Response timestamp")

class StockSearchResponse(BaseModel):
    """Stock search response"""
    success: bool = Field(..., description="Whether request succeeded")
    message: str = Field(..., description="Response message")
    data: List[StockInfo] = Field(..., description="Search results")
    count: int = Field(..., description="Result count")
    timestamp: str = Field(..., description="Response timestamp")
