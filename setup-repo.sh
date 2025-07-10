#!/bin/bash

# FastAPI Portfolio Service - Repository Setup Script
# This script helps set up a separate GitHub repository for Railway deployment

echo "🚀 FastAPI Portfolio Service - Repository Setup"
echo "============================================="

# Check if we're in the correct directory
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found. Please run this script from the fastapi-portfolio-service directory."
    exit 1
fi

echo "📁 Current directory: $(pwd)"
echo "✅ Found main.py - proceeding with setup"

# Initialize git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "🔧 Initializing git repository..."
    git init
    
    # Create initial commit
    echo "📝 Adding files to git..."
    git add .
    git commit -m "Initial commit: FastAPI Portfolio Service

🎯 Features:
- Portfolio risk analysis and optimization
- Monte Carlo simulation
- Market sentiment analysis
- Railway deployment configuration
- Comprehensive API documentation

🔧 Technology Stack:
- FastAPI + Python 3.12
- yfinance for market data
- numpy/pandas for calculations
- uvicorn ASGI server

🚀 Ready for Railway deployment"
    
    echo "✅ Git repository initialized with initial commit"
else
    echo "✅ Git repository already exists"
fi

# Instructions for GitHub setup
echo ""
echo "🔗 Next Steps - GitHub Repository Setup:"
echo "======================================="
echo ""
echo "1. Create a new GitHub repository:"
echo "   - Go to https://github.com/new"
echo "   - Repository name: fastapi-portfolio-service"
echo "   - Description: FastAPI microservice for portfolio analysis and risk calculation"
echo "   - Set as Public (for Railway deployment)"
echo "   - Do NOT initialize with README (we already have one)"
echo ""
echo "2. Add GitHub remote and push:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/fastapi-portfolio-service.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Railway Deployment:"
echo "   - Go to https://railway.app"
echo "   - Click 'New Project'"
echo "   - Select 'Deploy from GitHub repo'"
echo "   - Choose your fastapi-portfolio-service repository"
echo "   - Railway will automatically detect the configuration"
echo ""
echo "4. Environment Variables (Railway Dashboard):"
echo "   - RISK_FREE_RATE: 0.02 (optional, default value)"
echo "   - No other environment variables required"
echo ""
echo "5. Service URLs:"
echo "   - API Docs: https://your-service.railway.app/docs"
echo "   - Health Check: https://your-service.railway.app/health"
echo ""
echo "📋 Files created for Railway deployment:"
echo "- railway.json (Railway configuration)"
echo "- nixpacks.toml (Build configuration)"
echo "- Dockerfile (Alternative container build)"
echo "- README.md (Documentation)"
echo "- .gitignore (Updated for Railway)"
echo ""
echo "🎉 Setup complete! Follow the steps above to deploy to Railway."