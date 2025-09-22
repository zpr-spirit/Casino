"""
Quantitative Analysis API Endpoints
"""
from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Optional
from datetime import datetime

from app.models.schemas.quantitative import (
    QuantitativeAnalysisRequest,
    QuantitativeAnalysisResponse,
    StrategyListResponse,
    PerformanceMetricsInfo
)
from app.models.schemas.common import BaseResponse
from app.services.quantitative import QuantitativeAnalysisService

router = APIRouter(prefix="/quantitative", tags=["Quantitative Analysis"])

# Dependency injection
def get_quantitative_service() -> QuantitativeAnalysisService:
    """Get quantitative analysis service instance"""
    return QuantitativeAnalysisService()

@router.post("/analyze", response_model=QuantitativeAnalysisResponse)
async def run_quantitative_analysis(
    request: QuantitativeAnalysisRequest,
    service: QuantitativeAnalysisService = Depends(get_quantitative_service)
):
    """
    Run quantitative analysis
    
    - **strategy_name**: Strategy name
    - **parameters**: Strategy parameters
    - **start_date**: Start date
    - **end_date**: End date
    - **initial_capital**: Initial capital
    """
    try:
        result = await service.run_analysis(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/strategies", response_model=StrategyListResponse)
async def get_available_strategies(
    service: QuantitativeAnalysisService = Depends(get_quantitative_service)
):
    """
    Get available quantitative strategies
    """
    try:
        result = await service.get_strategies()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/strategies/{strategy_name}")
async def get_strategy_info(
    strategy_name: str,
    service: QuantitativeAnalysisService = Depends(get_quantitative_service)
):
    """
    Get strategy details
    
    - **strategy_name**: Strategy name
    """
    try:
        result = await service.get_strategy_info(strategy_name)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/backtest/{strategy_name}")
async def get_backtest_results(
    strategy_name: str,
    start_date: str = Query(..., description="Start date", example="2023-01-01"),
    end_date: str = Query(..., description="End date", example="2023-12-31"),
    initial_capital: float = Query(default=100000.0, description="Initial capital"),
    service: QuantitativeAnalysisService = Depends(get_quantitative_service)
):
    """
    Get strategy backtest results
    
    - **strategy_name**: Strategy name
    - **start_date**: Start date
    - **end_date**: End date
    - **initial_capital**: Initial capital
    """
    try:
        request = QuantitativeAnalysisRequest(
            strategy_name=strategy_name,
            start_date=start_date,
            end_date=end_date,
            initial_capital=initial_capital
        )
        result = await service.run_analysis(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/performance-metrics")
async def get_performance_metrics_info(
    service: QuantitativeAnalysisService = Depends(get_quantitative_service)
):
    """
    Get performance metrics info
    """
    try:
        result = await service.get_performance_metrics_info()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health", response_model=BaseResponse)
async def health_check():
    """Health check endpoint"""
    return BaseResponse(
        success=True,
        message="Quantitative analysis service running normally",
        timestamp=datetime.now().isoformat()
    )
