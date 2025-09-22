"""
Health Check API Endpoints
"""
from fastapi import APIRouter
from datetime import datetime

from app.models.schemas.common import HealthCheckResponse, APIInfo

router = APIRouter(prefix="/health", tags=["Health Check"])

@router.get("/", response_model=HealthCheckResponse)
async def health_check():
    """
    System health check
    """
    return HealthCheckResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        services={
            "stock_analysis": "running",
            "quantitative_analysis": "running",
            "database": "connected",
            "redis": "connected"
        },
        version="1.0.0"
    )

@router.get("/info", response_model=APIInfo)
async def api_info():
    """
    Get API information
    """
    return APIInfo(
        name="CSMAR Intelligent Financial Report Analysis Platform API",
        version="1.0.0",
        description="Backend API providing stock analysis and quantitative analysis services",
        status="running",
        timestamp=datetime.now().isoformat(),
        docs_url="/docs",
        redoc_url="/redoc"
    )
