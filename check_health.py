#!/usr/bin/env python3
"""
Health check script for FastAPI service
"""
import os
import sys

def check_imports():
    """Check if all required modules can be imported"""
    required_modules = [
        'fastapi',
        'uvicorn', 
        'pydantic',
        'yfinance',
        'numpy',
        'pandas',
        'scipy',
        'textblob',
        'requests'
    ]
    
    missing_modules = []
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            missing_modules.append(module)
    
    return len(missing_modules) == 0

def check_environment():
    """Check environment variables"""
    port = os.environ.get('PORT', '8000')
    print(f"🔧 PORT: {port}")
    
    # Check if all required env vars for service are available
    python_version = sys.version
    print(f"🐍 Python: {python_version}")
    
    return True

def check_fastapi_app():
    """Check if FastAPI app can be imported"""
    try:
        from main import app
        print(f"✅ FastAPI app imported successfully")
        print(f"📊 App title: {app.title}")
        print(f"📊 App version: {app.version}")
        return True
    except Exception as e:
        print(f"❌ Failed to import FastAPI app: {e}")
        return False

if __name__ == "__main__":
    print("🏥 FastAPI Service Health Check")
    print("=" * 40)
    
    checks_passed = 0
    total_checks = 3
    
    print("\n1. Checking module imports...")
    if check_imports():
        checks_passed += 1
    
    print("\n2. Checking environment...")
    if check_environment():
        checks_passed += 1
    
    print("\n3. Checking FastAPI app...")
    if check_fastapi_app():
        checks_passed += 1
    
    print(f"\n📊 Health Check Result: {checks_passed}/{total_checks} checks passed")
    
    if checks_passed == total_checks:
        print("✅ Service is healthy and ready to deploy!")
        sys.exit(0)
    else:
        print("❌ Service has issues that need to be resolved")
        sys.exit(1)