#!/bin/bash
set -e

echo "🚀 Starting FastAPI Portfolio Service"
echo "PORT: $PORT"
echo "Working directory: $(pwd)"
echo "Files: $(ls -la)"

# Install dependencies with pip (fallback)
if command -v uv >/dev/null 2>&1; then
    echo "📦 Using uv to install dependencies..."
    uv pip install -r requirements.txt --system
    echo "🎯 Starting with uv..."
    exec uv run --no-project uvicorn main:app --host 0.0.0.0 --port $PORT --log-level info
else
    echo "📦 Using pip to install dependencies..."
    pip install -r requirements.txt
    echo "🎯 Starting with python..."
    exec python -m uvicorn main:app --host 0.0.0.0 --port $PORT --log-level info
fi