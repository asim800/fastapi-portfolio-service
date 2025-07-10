#!/usr/bin/env python3
"""
Development server script with auto-reload
Uses uv if available, falls back to pip
"""
import os
import sys
import subprocess
import shutil

def main():
    print("🛠️ FastAPI Development Server")
    print("=" * 40)
    
    # Check if uv is available
    has_uv = shutil.which("uv") is not None
    
    if has_uv:
        print("✅ uv found - using uv for development")
        
        # Use the local pyproject.toml for uv
        if os.path.exists("pyproject-local.toml"):
            print("📦 Using pyproject-local.toml for uv development...")
            subprocess.run(["cp", "pyproject-local.toml", "pyproject.toml"], check=True)
            subprocess.run(["uv", "sync"], check=True)
        else:
            print("📦 Installing from requirements.txt with uv...")
            subprocess.run(["uv", "pip", "install", "-r", "requirements.txt"], check=True)
        
        # Start development server with uv
        print("🚀 Starting development server with auto-reload...")
        subprocess.run([
            "uv", "run", "uvicorn", "main:app", 
            "--reload", 
            "--host", "0.0.0.0", 
            "--port", "8000",
            "--log-level", "info"
        ], check=True)
        
    else:
        print("⚠️ uv not found - falling back to pip")
        
        # Install dependencies with pip
        print("📦 Installing dependencies with pip...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        
        # Start development server with python
        print("🚀 Starting development server...")
        os.environ["PORT"] = "8000"
        subprocess.run([sys.executable, "run_server.py"], check=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Development server stopped")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)