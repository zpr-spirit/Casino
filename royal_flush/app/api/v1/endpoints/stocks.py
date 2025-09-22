"""
Stock Analysis API Endpoints
"""
from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List, Optional
from datetime import datetime

from app.models.schemas.stock import (
    StockAnalysisRequest,
    StockAnalysisResponse,
    StockSearchRequest,
    StockSearchResponse,
    MarketType
)
from app.models.schemas.common import BaseResponse
from app.services.analisys_agent.analysis import StockAnalysisService

router = APIRouter(prefix="/stocks", tags=["Stock Analysis"])

# Dependency injection
def get_stock_service() -> StockAnalysisService:
    """Get stock analysis service instance"""
    return StockAnalysisService()

@router.post("/analyze", response_model=StockAnalysisResponse)
async def analyze_stock(
    request: StockAnalysisRequest,
    service: StockAnalysisService = Depends(get_stock_service)
):
    """
    Analyze single stock
    
    - **stock_code**: Stock code (e.g., 000001)
    - **market**: Market type (a_stock/hk_stock/us_stock)
    - **analysis_type**: Analysis type (basic/technical/fundamental)
    """
    try:
        result = await service.analyze_stock(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search", response_model=StockSearchResponse)
async def search_stocks(
    query: str = Query(..., description="Search keyword", example="Ping An"),
    market: MarketType = Query(..., description="Market type", example="a_stock"),
    limit: int = Query(default=10, description="Return limit"),
    service: StockAnalysisService = Depends(get_stock_service)
):
    """
    Search stocks
    
    - **query**: Search keyword (stock code or name)
    - **market**: Market type
    - **limit**: Return limit
    """
    try:
        search_request = StockSearchRequest(
            query=query,
            market=market,
            limit=limit
        )
        result = await service.search_stocks(search_request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/market/{market}/list")
async def get_market_stocks(
    market: MarketType,
    service: StockAnalysisService = Depends(get_stock_service)
):
    """
    Get market stock list
    
    - **market**: Market type
    """
    try:
        result = await service.get_market_stocks(market)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health", response_model=BaseResponse)
async def health_check():
    """Health check endpoint"""
    return BaseResponse(
        success=True,
        message="Stock analysis service running normally",
        timestamp=datetime.now().isoformat()
    )
