"""
Stock related data schemas
"""
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict, Generic, TypeVar
from enum import Enum
from datetime import datetime, timezone

# 类型定义
T = TypeVar('T')

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

class ApiResponse(BaseModel, Generic[T]):
    """API响应的标准格式"""
    success: bool = True
    message: str = "操作成功"
    data: Optional[T] = None
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class RunInfo(BaseModel):
    """运行信息模型"""
    run_id: str
    start_time: datetime
    end_time: Optional[datetime] = None
    status: str  # "running", "completed", "error"
    agents: List[str] = []


class StockAnalysisRequest(BaseModel):
    """Stock analysis request"""
    stock_code: str = Field(..., description="Stock code", example="000001")
    market: MarketType = Field(..., description="Market type", example="a_stock")
    analysis_type: AnalysisType = Field(default=AnalysisType.BASIC, description="Analysis type")
    show_reasoning: bool = Field(True,description="whether to display reasoning")
    start_date: str = Field(..., description="Start date", example="2024-01-01")
    end_date: str = Field(..., description="End date", example="2024-10-01")

class StockSearchRequest(BaseModel):
    """Stock search request"""
    query: str = Field(..., description="Search keyword", example="Ping An")
    market: MarketType = Field(..., description="Market type", example="a_stock")
    limit: int = Field(default=10, description="Return limit")

class AgentExecutionLog(BaseModel):
    """Agent执行日志"""
    agent_name: str = Field(..., description="Agent名称")
    run_id: str = Field(..., description="执行ID")
    timestamp_start: datetime = Field(..., description="开始时间")
    timestamp_end: datetime = Field(..., description="结束时间")
    input_state: Optional[Dict[str, Any]] = Field(None, description="输入状态")
    output_state: Optional[Dict[str, Any]] = Field(None, description="输出状态")
    reasoning_details: Optional[Any] = Field(None, description="推理细节")
    terminal_outputs: List[str] = Field(
        default_factory=list, description="终端输出")

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
    run_id: str = Field(..., description="Run ID")
    ticker: str = Field(..., description="Ticker")
    status: str = Field(..., description="Status")
    message: str = Field(..., description="Message")
    submitted_at: datetime = Field(..., description="Submitted at")

class StockSearchResponse(BaseModel):
    """Stock search response"""
    success: bool = Field(..., description="Whether request succeeded")
    message: str = Field(..., description="Response message")
    data: List[StockInfo] = Field(..., description="Search results")
    count: int = Field(..., description="Result count")
    timestamp: str = Field(..., description="Response timestamp")
