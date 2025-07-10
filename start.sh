#!/bin/bash
set -e

echo "🚀 Starting FastAPI Portfolio Service"
echo "PORT: $PORT"
echo "Working directory: $(pwd)"

# Start the FastAPI server with uv
exec uv run uvicorn main:app --host 0.0.0.0 --port $PORT --log-level info