#!/usr/bin/env python3
"""
New version API test script
"""

import requests
import json
from datetime import datetime

# API base URL
BASE_URL = "http://localhost:8000"

def test_health_check():
    """Test health check endpoint"""
    print("🔍 Testing health check endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_api_info():
    """Test API info endpoint"""
    print("\n📋 Testing API info endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ API info test failed: {e}")
        return False

def test_stock_analysis():
    """Test stock analysis endpoint"""
    print("\n📊 Testing stock analysis endpoint...")
    
    # Test stock analysis
    analysis_data = {
        "stock_code": "000001",
        "market": "a_stock",
        "analysis_type": "basic"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/v1/stocks/analyze",
            json=analysis_data
        )
        print(f"Status code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Stock analysis test failed: {e}")
        return False

def test_stock_search():
    """Test stock search endpoint"""
    print("\n🔍 Testing stock search endpoint...")
    
    try:
        response = requests.get(
            f"{BASE_URL}/api/v1/stocks/search",
            params={"query": "Ping An", "market": "a_stock", "limit": 5}
        )
        print(f"Status code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Stock search test failed: {e}")
        return False

def test_quantitative_analysis():
    """Test quantitative analysis endpoint"""
    print("\n🔢 Testing quantitative analysis endpoint...")
    
    # Test quantitative analysis
    analysis_data = {
        "strategy_name": "momentum_strategy",
        "parameters": {},
        "start_date": "2023-01-01",
        "end_date": "2023-12-31",
        "initial_capital": 100000.0
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/v1/quantitative/analyze",
            json=analysis_data
        )
        print(f"Status code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Quantitative analysis test failed: {e}")
        return False

def test_get_strategies():
    """Test get strategies list endpoint"""
    print("\n📋 Testing get strategies list endpoint...")
    
    try:
        response = requests.get(f"{BASE_URL}/api/v1/quantitative/strategies")
        print(f"Status code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Get strategies list test failed: {e}")
        return False

def test_v1_health():
    """Test v1 health check endpoint"""
    print("\n🏥 Testing v1 health check endpoint...")
    
    try:
        response = requests.get(f"{BASE_URL}/api/v1/health/")
        print(f"Status code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ v1 health check test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Starting CSMAR API service tests (new version)")
    print("=" * 60)
    
    tests = [
        ("Health Check", test_health_check),
        ("API Info", test_api_info),
        ("Stock Analysis", test_stock_analysis),
        ("Stock Search", test_stock_search),
        ("Quantitative Analysis", test_quantitative_analysis),
        ("Get Strategies", test_get_strategies),
        ("v1 Health Check", test_v1_health)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        if test_func():
            print(f"✅ {test_name} test passed")
            passed += 1
        else:
            print(f"❌ {test_name} test failed")
    
    print(f"\n{'='*60}")
    print(f"📊 Test results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 All tests passed! API service running normally")
    else:
        print("⚠️  Some tests failed, please check service status")

if __name__ == "__main__":
    main()
