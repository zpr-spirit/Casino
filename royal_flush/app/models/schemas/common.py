"""
Common data schemas
"""
from pydantic import BaseModel, Field
from typing import Optional, Any, Dict
from datetime import datetime

class BaseResponse(BaseModel):
    """Base response model"""
    success: bool = Field(..., description="Whether request succeeded")
    message: str = Field(..., description="Response message")
    timestamp: str = Field(..., description="Response timestamp")

class ErrorResponse(BaseResponse):
    """Error response model"""
    success: bool = Field(False, description="Whether request succeeded")
    error_code: Optional[str] = Field(None, description="Error code")
    details: Optional[Dict[str, Any]] = Field(None, description="Error details")

class HealthCheckResponse(BaseModel):
    """Health check response"""
    status: str = Field(..., description="Service status")
    timestamp: str = Field(..., description="Check time")
    services: Dict[str, str] = Field(..., description="Service statuses")
    version: str = Field(..., description="API version")

class PaginationParams(BaseModel):
    """Pagination parameters"""
    page: int = Field(default=1, ge=1, description="Page number")
    size: int = Field(default=10, ge=1, le=100, description="Page size")
    sort_by: Optional[str] = Field(None, description="Sort field")
    sort_order: str = Field(default="desc", description="Sort order")

class PaginatedResponse(BaseModel):
    """Paginated response"""
    items: list = Field(..., description="Data items")
    total: int = Field(..., description="Total count")
    page: int = Field(..., description="Current page")
    size: int = Field(..., description="Page size")
    pages: int = Field(..., description="Total pages")
    has_next: bool = Field(..., description="Has next page")
    has_prev: bool = Field(..., description="Has previous page")

class APIInfo(BaseModel):
    """API information"""
    name: str = Field(..., description="API name")
    version: str = Field(..., description="API version")
    description: str = Field(..., description="API description")
    status: str = Field(..., description="API status")
    timestamp: str = Field(..., description="Timestamp")
    docs_url: str = Field(..., description="Documentation URL")
    redoc_url: str = Field(..., description="ReDoc URL")
