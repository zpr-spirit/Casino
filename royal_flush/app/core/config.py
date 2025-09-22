"""
Application Configuration Module
"""
from pydantic_settings import BaseSettings
from typing import List, Optional
import os

class Settings(BaseSettings):
    """Application configuration class"""
    
    # Application basic info
    APP_NAME: str = "CSMAR Intelligent Financial Report Analysis Platform API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Backend API providing stock analysis and quantitative analysis services"
    
    # Server configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # API configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "CSMAR API"
    
    # CORS configuration
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]
    
    # Database configuration (reserved)
    DATABASE_URL: Optional[str] = None
    
    # Redis configuration (reserved)
    REDIS_URL: Optional[str] = None
    
    # Logging configuration
    LOG_LEVEL: str = "INFO"
    
    # Security configuration
    SECRET_KEY: str = "your-secret-key-here"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # External API configuration (reserved)
    STOCK_DATA_API_URL: Optional[str] = None
    STOCK_DATA_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Create global configuration instance
settings = Settings()
