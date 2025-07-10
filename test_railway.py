#!/usr/bin/env python3
"""
Test script to check Railway deployment
"""
import requests
import sys

def test_railway_service(base_url):
    """Test Railway service endpoints"""
    print(f"🧪 Testing Railway service: {base_url}")
    print("=" * 50)
    
    # Test endpoints
    endpoints = [
        "/",
        "/health", 
        "/docs"
    ]
    
    for endpoint in endpoints:
        url = f"{base_url}{endpoint}"
        print(f"\n📡 Testing: {url}")
        
        try:
            response = requests.get(url, timeout=10)
            print(f"✅ Status: {response.status_code}")
            if response.status_code == 200:
                print(f"📄 Response: {response.text[:200]}...")
            else:
                print(f"❌ Error: {response.text[:200]}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Connection Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    # Test with different possible URLs
    base_urls = [
        "https://fastapi-portfolio-service-production.up.railway.app",
        "https://fastapi-portfolio-service.railway.app", 
        "https://fastapi-portfolio-service-production.railway.app"
    ]
    
    for base_url in base_urls:
        test_railway_service(base_url)
        print("\n" + "="*50 + "\n")