#!/usr/bin/env python3
"""
Simple Railway deployment script
This installs dependencies and starts the FastAPI server
"""
import subprocess
import sys
import os

def main():
    print("🚂 Railway FastAPI Deployment")
    print("=" * 40)
    
    # Check if we're in Docker (dependencies already installed)
    in_docker = os.path.exists("/.dockerenv")
    
    if not in_docker:
        # Install dependencies if not in Docker
        print("📦 Installing dependencies...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "--upgrade", "pip", "setuptools", "wheel"
        ])
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "-r", "requirements.txt", "--no-cache-dir"
        ])
    else:
        print("🐳 Running in Docker - dependencies already installed")
    
    # Import and run the server
    print("🚀 Starting FastAPI server...")
    from run_server import main as run_main
    run_main()

if __name__ == "__main__":
    main()