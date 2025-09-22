"""
Quantitative analysis related entity models
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime

class StrategyEntity(BaseModel):
    """Strategy entity"""
    id: Optional[int] = None
    name: str = Field(..., description="Strategy name")
    display_name: str = Field(..., description="Display name")
    description: str = Field(..., description="Strategy description")
    risk_level: str = Field(..., description="Risk level")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Strategy parameters")
    is_active: bool = Field(True, description="Whether active")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class BacktestEntity(BaseModel):
    """Backtest entity"""
    id: Optional[int] = None
    strategy_name: str = Field(..., description="Strategy name")
    start_date: str = Field(..., description="Start date")
    end_date: str = Field(..., description="End date")
    initial_capital: float = Field(..., description="Initial capital")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Strategy parameters")
    results: Optional[Dict[str, Any]] = Field(None, description="Backtest results")
    status: str = Field("pending", description="Status")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class PerformanceMetricsEntity(BaseModel):
    """Performance metrics entity"""
    id: Optional[int] = None
    backtest_id: int = Field(..., description="Backtest ID")
    total_return: Optional[float] = Field(None, description="Total return")
    annual_return: Optional[float] = Field(None, description="Annual return")
    max_drawdown: Optional[float] = Field(None, description="Max drawdown")
    sharpe_ratio: Optional[float] = Field(None, description="Sharpe ratio")
    sortino_ratio: Optional[float] = Field(None, description="Sortino ratio")
    calmar_ratio: Optional[float] = Field(None, description="Calmar ratio")
    win_rate: Optional[float] = Field(None, description="Win rate")
    profit_factor: Optional[float] = Field(None, description="Profit factor")
    total_trades: Optional[int] = Field(None, description="Total trades")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
