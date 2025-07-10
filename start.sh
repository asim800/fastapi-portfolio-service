#!/bin/bash

# FastAPI Portfolio Service - Railway Startup Script
# This script handles the startup process for Railway deployment

echo "🚀 Starting FastAPI Portfolio Service on Railway"
echo "================================================"

# Set default port if not provided
export PORT=${PORT:-8000}

# Set default risk-free rate if not provided
export RISK_FREE_RATE=${RISK_FREE_RATE:-0.02}

# Log environment info
echo "📊 Environment Configuration:"
echo "   - PORT: $PORT"
echo "   - RISK_FREE_RATE: $RISK_FREE_RATE"
echo "   - Python Version: $(python --version)"
echo "   - Working Directory: $(pwd)"

# Check if required files exist
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found in $(pwd)"
    exit 1
fi

if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found in $(pwd)"
    exit 1
fi

echo "✅ Required files found"

# Start the FastAPI server
echo "🎯 Starting FastAPI server..."
echo "   - Host: 0.0.0.0"
echo "   - Port: $PORT"
echo "   - Application: main:app"

# Use uv to run the application
exec uv run uvicorn main:app --host 0.0.0.0 --port $PORT --log-level info