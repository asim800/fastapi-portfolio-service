#!/usr/bin/env python3
"""
Railway startup script for FastAPI Portfolio Service
Provides better logging and error handling for Railway deployment
"""
import os
import sys
import logging
import uvicorn

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main startup function"""
    try:
        # Get port from environment
        port = int(os.environ.get("PORT", 8000))
        host = "0.0.0.0"
        
        logger.info("🚀 Starting FastAPI Portfolio Service on Railway")
        logger.info(f"📡 Host: {host}")
        logger.info(f"🔌 Port: {port}")
        logger.info(f"🐍 Python: {sys.version}")
        logger.info(f"📁 Working Directory: {os.getcwd()}")
        
        # Check if main app can be imported
        try:
            from main import app
            logger.info(f"✅ FastAPI app imported: {app.title} v{app.version}")
        except Exception as e:
            logger.error(f"❌ Failed to import FastAPI app: {e}")
            sys.exit(1)
        
        # Start the server
        logger.info("🎯 Starting uvicorn server...")
        uvicorn.run(
            "main:app",
            host=host,
            port=port,
            log_level="info",
            access_log=True
        )
        
    except Exception as e:
        logger.error(f"❌ Failed to start service: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()