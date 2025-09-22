"""
Quantitative analysis related data schemas
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List

class QuantitativeAnalysisRequest(BaseModel):
    """Quantitative analysis request"""
    strategy_name: str = Field(..., description="Strategy name", example="momentum_strategy")
    parameters: Dict[str, Any] = Field(default={}, description="Strategy parameters")
    start_date: str = Field(..., description="Start date", example="2023-01-01")
    end_date: str = Field(..., description="End date", example="2023-12-31")
    initial_capital: float = Field(default=100000.0, description="Initial capital")

class StrategyInfo(BaseModel):
    """Strategy information"""
    name: str = Field(..., description="Strategy name")
    display_name: str = Field(..., description="Display name")
    description: str = Field(..., description="Strategy description")
    risk_level: str = Field(..., description="Risk level")
    parameters_schema: Optional[Dict[str, Any]] = Field(None, description="Parameter schema")

class BacktestResults(BaseModel):
    """Backtest results"""
    total_return: float = Field(..., description="Total return")
    annual_return: float = Field(..., description="Annual return")
    max_drawdown: float = Field(..., description="Max drawdown")
    sharpe_ratio: float = Field(..., description="Sharpe ratio")
    sortino_ratio: float = Field(..., description="Sortino ratio")
    calmar_ratio: float = Field(..., description="Calmar ratio")
    win_rate: float = Field(..., description="Win rate")
    profit_factor: float = Field(..., description="Profit factor")
    total_trades: int = Field(..., description="Total trades")
    avg_trade_duration: int = Field(..., description="Average trade duration")

class RiskMetrics(BaseModel):
    """Risk metrics"""
    var_95: float = Field(..., description="95% VaR")
    var_99: float = Field(..., description="99% VaR")
    expected_shortfall: float = Field(..., description="Expected shortfall")
    volatility: float = Field(..., description="Volatility")
    beta: float = Field(..., description="Beta coefficient")
    correlation_market: float = Field(..., description="Market correlation")

class FactorAnalysis(BaseModel):
    """Factor analysis"""
    momentum_factor: float = Field(..., description="Momentum factor")
    value_factor: float = Field(..., description="Value factor")
    quality_factor: float = Field(..., description="Quality factor")
    size_factor: float = Field(..., description="Size factor")
    volatility_factor: float = Field(..., description="Volatility factor")

class TradingSignal(BaseModel):
    """Trading signal"""
    date: str = Field(..., description="Date")
    symbol: str = Field(..., description="Symbol")
    action: str = Field(..., description="Action")
    price: float = Field(..., description="Price")
    quantity: int = Field(..., description="Quantity")
    confidence: float = Field(..., description="Confidence")
    reason: str = Field(..., description="Reason")

class TradingSignals(BaseModel):
    """Trading signals collection"""
    total_signals: int = Field(..., description="Total signals")
    buy_signals: int = Field(..., description="Buy signals")
    sell_signals: int = Field(..., description="Sell signals")
    hold_signals: int = Field(..., description="Hold signals")
    recent_signals: List[TradingSignal] = Field(..., description="Recent signals")

class PositionAnalysis(BaseModel):
    """Position analysis"""
    total_positions: int = Field(..., description="Total positions")
    long_positions: int = Field(..., description="Long positions")
    short_positions: int = Field(..., description="Short positions")
    cash_ratio: float = Field(..., description="Cash ratio")
    leverage_ratio: float = Field(..., description="Leverage ratio")
    concentration_risk: float = Field(..., description="Concentration risk")

class QuantitativeAnalysisResult(BaseModel):
    """Quantitative analysis results"""
    strategy_name: str = Field(..., description="Strategy name")
    parameters: Dict[str, Any] = Field(..., description="Strategy parameters")
    backtest_period: Dict[str, str] = Field(..., description="Backtest period")
    initial_capital: float = Field(..., description="Initial capital")
    backtest_results: BacktestResults = Field(..., description="Backtest results")
    risk_metrics: RiskMetrics = Field(..., description="Risk metrics")
    factor_analysis: FactorAnalysis = Field(..., description="Factor analysis")
    trading_signals: TradingSignals = Field(..., description="Trading signals")
    position_analysis: PositionAnalysis = Field(..., description="Position analysis")
    recommendations: Dict[str, str] = Field(..., description="Investment recommendations")

class QuantitativeAnalysisResponse(BaseModel):
    """Quantitative analysis response"""
    success: bool = Field(..., description="Whether request succeeded")
    message: str = Field(..., description="Response message")
    data: Optional[QuantitativeAnalysisResult] = Field(None, description="Analysis result")
    timestamp: str = Field(..., description="Response timestamp")

class StrategyListResponse(BaseModel):
    """Strategy list response"""
    success: bool = Field(..., description="Whether request succeeded")
    message: str = Field(..., description="Response message")
    data: List[StrategyInfo] = Field(..., description="Strategy list")
    count: int = Field(..., description="Strategy count")
    timestamp: str = Field(..., description="Response timestamp")

class PerformanceMetricsInfo(BaseModel):
    """Performance metrics information"""
    return_metrics: Dict[str, str] = Field(..., description="Return metrics")
    risk_metrics: Dict[str, str] = Field(..., description="Risk metrics")
    trading_metrics: Dict[str, str] = Field(..., description="Trading metrics")
