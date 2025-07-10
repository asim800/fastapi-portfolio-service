# Railway Deployment Guide

## Quick Deploy Steps

### 1. Create GitHub Repository

```bash
# Navigate to the service directory
cd services/fastapi-portfolio-service

# Run the setup script
./setup-repo.sh
```

### 2. Create GitHub Repository Online

1. Go to [GitHub](https://github.com/new)
2. Create repository named: `fastapi-portfolio-service`
3. Set as **Public** (required for Railway)
4. **Do NOT** initialize with README

### 3. Push to GitHub

```bash
# Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/fastapi-portfolio-service.git

# Push to main branch
git branch -M main
git push -u origin main
```

### 4. Deploy to Railway

1. Go to [Railway](https://railway.app)
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your `fastapi-portfolio-service` repository
5. Railway will automatically detect the configuration

### 5. Configure Environment Variables (Optional)

In Railway dashboard:
- `RISK_FREE_RATE`: `0.02` (default value)

### 6. Access Your Service

- **API Documentation**: `https://your-service.railway.app/docs`
- **Health Check**: `https://your-service.railway.app/health`
- **Service Status**: `https://your-service.railway.app/`

## Configuration Files

### Railway Configuration (`railway.json`)
```json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "uvicorn main:app --host 0.0.0.0 --port $PORT",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

### Nixpacks Configuration (`nixpacks.toml`)
```toml
[phases.setup]
nixPkgs = ["python312", "gcc"]

[phases.install]
cmds = [
    "pip install uv",
    "uv sync --frozen"
]

[start]
cmd = "uv run uvicorn main:app --host 0.0.0.0 --port $PORT"
```

## Testing the Deployment

### Health Check
```bash
curl https://your-service.railway.app/health
```

### Portfolio Analysis
```bash
curl -X POST "https://your-service.railway.app/portfolio/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "assets": [
      {"symbol": "AAPL", "shares": 100},
      {"symbol": "GOOGL", "shares": 50}
    ]
  }'
```

## Troubleshooting

### Build Issues
- Check Railway logs in the dashboard
- Ensure `pyproject.toml` and `uv.lock` are committed (uv.lock is required for reproducible builds)
- Verify Python 3.12 compatibility
- Run `uv sync --frozen` locally to verify lock file is valid

### Runtime Issues
- Check service logs for errors
- Verify API endpoints with `/docs`
- Test health check endpoint

### Common Solutions
1. **Build fails**: Check dependencies in `pyproject.toml`
2. **Service won't start**: Check `PORT` environment variable
3. **API errors**: Review logs for Python exceptions

## Monitoring

### Railway Dashboard
- View deployment logs
- Monitor resource usage
- Check service health

### API Endpoints
- `/health` - Service health check
- `/docs` - Interactive API documentation
- `/redoc` - Alternative API documentation

## Scaling

Railway automatically handles:
- Auto-scaling based on traffic
- Load balancing
- SSL/TLS certificates
- Custom domains (if needed)

## Cost Optimization

- Railway charges based on usage
- Service automatically sleeps when idle
- No additional configuration needed for cost optimization