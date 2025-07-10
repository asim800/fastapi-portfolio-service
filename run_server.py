#!/usr/bin/env python3
"""
Simple Python script to start the FastAPI server
Uses pip for Railway deployment, can detect uv for local development
"""
import os
import sys
import subprocess

def main():
    # Get port from environment
    port = os.environ.get("PORT", "8000")
    is_railway = os.environ.get("RAILWAY_ENVIRONMENT") is not None
    
    print(f"🚀 Starting FastAPI Portfolio Service")
    print(f"📡 Port: {port}")
    print(f"📁 Working directory: {os.getcwd()}")
    print(f"🐍 Python executable: {sys.executable}")
    print(f"🚂 Railway environment: {is_railway}")
    
    # Check if uvicorn is available
    try:
        import uvicorn
        print(f"✅ uvicorn found: {uvicorn.__version__}")
    except ImportError:
        print("❌ uvicorn not found, installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "uvicorn[standard]"])
        import uvicorn
    
    # Import the FastAPI app
    try:
        from main import app
        print(f"✅ FastAPI app imported: {app.title}")
    except ImportError as e:
        print(f"❌ Failed to import FastAPI app: {e}")
        sys.exit(1)
    
    # Start the server
    print(f"🎯 Starting uvicorn server on port {port}")
    
    if is_railway:
        print("🚂 Running in Railway environment with pip")
    else:
        print("🛠️ Running in local development environment")
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(port),
        log_level="info",
        reload=not is_railway  # Enable reload only for local development
    )

if __name__ == "__main__":
    main()