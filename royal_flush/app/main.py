"""
Casino Backend API Main Application
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from datetime import datetime

from app.core.config import settings
from app.core.security import create_access_token
from app.utils.logger import get_logger
from app.api.v1.endpoints import stocks, quantitative, health
from app.models.schemas.common import APIInfo, HealthCheckResponse

# Get logger
logger = get_logger(__name__)

# Application lifecycle management
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifecycle management"""
    # Startup
    logger.info("🚀 FastAPI application starting...")
    logger.info("📊 Stock analysis service ready")
    logger.info("🔢 Quantitative analysis service ready")
    logger.info(f"🌐 Service URL: http://{settings.HOST}:{settings.PORT}")
    logger.info(f"📖 API docs: http://{settings.HOST}:{settings.PORT}/docs")
    
    yield
    
    # Shutdown
    logger.info("🛑 FastAPI application shutting down...")

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(
    stocks.router,
    prefix=settings.API_V1_STR,
    tags=["Stock Analysis"]
)

app.include_router(
    quantitative.router,
    prefix=settings.API_V1_STR,
    tags=["Quantitative Analysis"]
)

app.include_router(
    health.router,
    prefix=settings.API_V1_STR,
    tags=["Health Check"]
)

# Root path
@app.get("/", response_model=APIInfo)
async def root():
    """Root path - API information"""
    return APIInfo(
        name=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
        status="running",
        timestamp=datetime.now().isoformat(),
        docs_url="/docs",
        redoc_url="/redoc"
    )

# Global exception handling
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    logger.error(f"Global exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error",
            "error": str(exc),
            "timestamp": datetime.now().isoformat()
        }
    )

# 404 handling
@app.exception_handler(404)
async def not_found_handler(request, exc):
    """404 exception handler"""
    logger.warning(f"404 error: {request.url}")
    return JSONResponse(
        status_code=404,
        content={
            "success": False,
            "message": "Resource not found",
            "path": str(request.url),
            "timestamp": datetime.now().isoformat()
        }
    )

# Health check (legacy compatibility)
@app.get("/health")
async def health_check_legacy():
    """Health check endpoint (legacy compatibility)"""
    return HealthCheckResponse(
        status="healthy",
        timestamp=datetime.now().isoformat(),
        services={
            "stock_analysis": "running",
            "quantitative_analysis": "running",
            "database": "connected",
            "redis": "connected"
        },
        version=settings.APP_VERSION
    )

if __name__ == "__main__":
    import uvicorn
    
    logger.info("🌟 Starting CSMAR Intelligent Financial Report Analysis Platform API Service")
    logger.info("=" * 50)
    logger.info(f"📖 API docs: http://{settings.HOST}:{settings.PORT}/docs")
    logger.info(f"📚 ReDoc docs: http://{settings.HOST}:{settings.PORT}/redoc")
    logger.info(f"🔍 Health check: http://{settings.HOST}:{settings.PORT}/health")
    logger.info("=" * 50)
    
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        log_level=settings.LOG_LEVEL.lower()
    )
