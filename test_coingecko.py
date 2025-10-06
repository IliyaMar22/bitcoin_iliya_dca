#!/usr/bin/env python3
"""
Test CoinGecko API to fetch Bitcoin historical data
"""

import requests
import json
from datetime import datetime

def test_coingecko_api():
    api_key = "CG-UastZQrBeQqKdGePWbVaouAZ"
    
    print("Testing CoinGecko API...")
    print("=" * 60)
    
    # Test 1: Get current Bitcoin price
    print("\n1. Current Bitcoin Price (EUR):")
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {
            "ids": "bitcoin",
            "vs_currencies": "eur,usd",
            "include_market_cap": "true",
            "include_24hr_change": "true"
        }
        headers = {
            "x-cg-demo-api-key": api_key
        }
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 2: Get Bitcoin market data
    print("\n2. Bitcoin Market Data:")
    try:
        url = "https://api.coingecko.com/api/v3/coins/bitcoin"
        headers = {
            "x-cg-demo-api-key": api_key
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(f"Name: {data['name']}")
        print(f"Symbol: {data['symbol']}")
        print(f"Genesis Date: {data.get('genesis_date', 'N/A')}")
        print(f"Market Cap Rank: {data['market_cap_rank']}")
        print(f"Current Price (EUR): €{data['market_data']['current_price']['eur']:,.2f}")
        print(f"Current Price (USD): ${data['market_data']['current_price']['usd']:,.2f}")
        print(f"Market Cap (EUR): €{data['market_data']['market_cap']['eur']:,.0f}")
        print(f"Total Volume (EUR): €{data['market_data']['total_volume']['eur']:,.0f}")
        print(f"All-Time High (EUR): €{data['market_data']['ath']['eur']:,.2f}")
        print(f"All-Time High Date: {data['market_data']['ath_date']['eur']}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 3: Get historical market data (last 1 year as test)
    print("\n3. Historical Price Data (Sample - Last 30 days):")
    try:
        url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
        params = {
            "vs_currency": "eur",
            "days": "30",
            "interval": "daily"
        }
        headers = {
            "x-cg-demo-api-key": api_key
        }
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        prices = data['prices']
        print(f"Total data points: {len(prices)}")
        print(f"First price: €{prices[0][1]:,.2f} on {datetime.fromtimestamp(prices[0][0]/1000).strftime('%Y-%m-%d')}")
        print(f"Last price: €{prices[-1][1]:,.2f} on {datetime.fromtimestamp(prices[-1][0]/1000).strftime('%Y-%m-%d')}")
        print(f"Price change: {((prices[-1][1] - prices[0][1]) / prices[0][1] * 100):+.2f}%")
    except Exception as e:
        print(f"Error: {e}")
    
    # Test 4: Check if we can get full historical data
    print("\n4. Full Historical Data (All Time):")
    try:
        url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
        params = {
            "vs_currency": "eur",
            "days": "max",  # Get all available data
            "interval": "daily"
        }
        headers = {
            "x-cg-demo-api-key": api_key
        }
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        prices = data['prices']
        print(f"✅ Total data points available: {len(prices)}")
        print(f"📅 First data point: €{prices[0][1]:,.2f} on {datetime.fromtimestamp(prices[0][0]/1000).strftime('%Y-%m-%d')}")
        print(f"📅 Last data point: €{prices[-1][1]:,.2f} on {datetime.fromtimestamp(prices[-1][0]/1000).strftime('%Y-%m-%d')}")
        
        # Calculate some basic statistics
        first_price = prices[0][1]
        last_price = prices[-1][1]
        years = (prices[-1][0] - prices[0][0]) / (1000 * 60 * 60 * 24 * 365.25)
        cagr = (pow(last_price / first_price, 1 / years) - 1) * 100
        
        print(f"\n📊 Quick Stats:")
        print(f"Time Period: {years:.1f} years")
        print(f"Total Return: {((last_price - first_price) / first_price * 100):,.1f}%")
        print(f"CAGR: {cagr:.2f}%")
        
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "=" * 60)
    print("✅ CoinGecko API test complete!")

if __name__ == "__main__":
    test_coingecko_api()

