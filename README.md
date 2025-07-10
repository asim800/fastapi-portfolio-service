# FastAPI Portfolio Service

A comprehensive FastAPI microservice for portfolio analysis, risk calculation, and financial data processing.

## Features

- **Portfolio Risk Analysis**: Calculate VaR, volatility, Sharpe ratio, and beta
- **Portfolio Optimization**: Modern Portfolio Theory-based optimization
- **Monte Carlo Simulation**: Future portfolio projections
- **Market Sentiment Analysis**: Sentiment scoring and analysis
- **Market Data Integration**: Real-time data via yfinance
- **Comprehensive API**: RESTful endpoints for all financial calculations

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd fastapi-portfolio-service
   ```

2. **Install dependencies**
   
   **For local development (recommended - uses uv):**
   ```bash
   pip install uv
   python dev.py  # Automatically sets up uv environment
   ```
   
   **For Railway-compatible setup (uses pip):**
   ```bash
   pip install -r requirements.txt
   python run_server.py
   ```

3. **Run the development server**
   
   **Auto-setup development (recommended):**
   ```bash
   python dev.py  # Auto-detects uv, sets up environment, enables reload
   ```
   
   **Manual uv setup:**
   ```bash
   cp pyproject-local.toml pyproject.toml
   uv sync
   uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   
   **Manual pip setup:**
   ```bash
   pip install -r requirements.txt
   python run_server.py
   ```

4. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

### Railway Deployment

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)

1. **Connect to Railway**
   - Fork this repository
   - Connect your GitHub repository to Railway
   - Railway will automatically detect the configuration

2. **Environment Variables**
   - No additional environment variables required for basic functionality
   - Optional: `RISK_FREE_RATE` (default: 0.02)

3. **Deploy**
   - Railway will automatically build and deploy using the provided configuration
   - The service will be available at your Railway domain

## API Endpoints

### Health & Status
- `GET /` - Service status
- `GET /health` - Health check

### Portfolio Analysis
- `POST /portfolio/analyze` - Comprehensive portfolio analysis
- `POST /portfolio/risk` - Risk metrics calculation
- `POST /portfolio/sharpe` - Sharpe ratio calculation
- `POST /portfolio/optimize` - Portfolio optimization
- `POST /portfolio/monte-carlo` - Monte Carlo simulation

### Market Data
- `POST /portfolio/market-data` - Fetch market data
- `POST /market/sentiment` - Market sentiment analysis

## Request Examples

### Portfolio Analysis
```bash
curl -X POST "http://localhost:8000/portfolio/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "assets": [
      {"symbol": "AAPL", "shares": 100},
      {"symbol": "GOOGL", "shares": 50}
    ],
    "requestId": "test-123"
  }'
```

### Portfolio Optimization
```bash
curl -X POST "http://localhost:8000/portfolio/optimize" \
  -H "Content-Type: application/json" \
  -d '{
    "assets": [
      {"symbol": "AAPL", "shares": 100},
      {"symbol": "GOOGL", "shares": 50},
      {"symbol": "MSFT", "shares": 75}
    ],
    "objective": "max_sharpe",
    "risk_tolerance": 0.6,
    "requestId": "opt-123"
  }'
```

## Configuration

### Railway Configuration

The service includes several deployment configurations:

- **railway.json**: Railway-specific deployment settings
- **nixpacks.toml**: Nixpacks build configuration
- **Dockerfile**: Docker containerization (alternative)

### Dependencies

- **Python 3.12+**: Required Python version
- **FastAPI**: Web framework
- **yfinance**: Market data fetching
- **numpy/pandas**: Data processing
- **scipy**: Optimization algorithms
- **uvicorn**: ASGI server

## Architecture

### Service Design
- **Microservice Architecture**: Standalone service for portfolio analysis
- **RESTful API**: Standard HTTP endpoints
- **Async/Await**: Non-blocking request handling
- **Comprehensive Logging**: Request tracking and analytics
- **CORS Support**: Cross-origin resource sharing enabled

### Data Processing
- **Real-time Market Data**: Via yfinance integration
- **Risk Calculations**: VaR, volatility, beta, Sharpe ratio
- **Portfolio Optimization**: Modern Portfolio Theory implementation
- **Monte Carlo Simulation**: Statistical modeling for projections
- **Sentiment Analysis**: Market sentiment scoring

## Performance Features

- **Request Timing**: Automatic timing headers
- **Request ID Tracking**: Optional request correlation
- **Comprehensive Logging**: Detailed request/response logging
- **Error Handling**: Graceful error responses
- **Data Caching**: Market data optimization

## Development

### Running Tests
```bash
uv run pytest
```

### Code Quality
- **Type Hints**: Full type annotation support
- **Pydantic Models**: Data validation and serialization
- **Error Handling**: Comprehensive exception management
- **Logging**: Structured logging throughout

### API Documentation
- **OpenAPI/Swagger**: Automatic API documentation at `/docs`
- **Redoc**: Alternative documentation at `/redoc`
- **Type Safety**: Pydantic model validation

## Production Considerations

### Scaling
- **Stateless Design**: No local state storage
- **Horizontal Scaling**: Multiple instance support
- **Load Balancing**: Compatible with standard load balancers

### Security
- **CORS Configuration**: Configurable cross-origin policies
- **Input Validation**: Comprehensive request validation
- **Error Sanitization**: No sensitive data in error responses

### Monitoring
- **Health Checks**: Built-in health endpoints
- **Request Logging**: Detailed request analytics
- **Performance Metrics**: Request timing and throughput

## License

This project is part of the finance-app ecosystem.

## Support

For issues and questions, please refer to the main project documentation or create an issue in the repository.