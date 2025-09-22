#!/usr/bin/env python3
"""
CSMAR Intelligent Financial Report Analysis Platform API startup script (new version)
"""

import uvicorn
import sys
import os

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print("🌟 Starting CSMAR Intelligent Financial Report Analysis Platform API Service (new version)")
    print("=" * 60)
    print("📖 API docs: http://localhost:8000/docs")
    print("📚 ReDoc docs: http://localhost:8000/redoc")
    print("🔍 Health check: http://localhost:8000/health")
    print("=" * 60)
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
        access_log=True
    )
