"""
CSMAR Intelligent Financial Report Analysis Platform API Entry Point
"""
import uvicorn
from app.main import app
from app.core.config import settings
from app.utils.logger import get_logger

# Get logger
logger = get_logger(__name__)

if __name__ == "__main__":
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