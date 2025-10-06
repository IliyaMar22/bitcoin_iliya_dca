#!/usr/bin/env python3
"""
Test yfinance to fetch Bitcoin historical data
"""

import yfinance as yf
import pandas as pd
from datetime import datetime
import numpy as np

def test_bitcoin_data():
    print("Testing yfinance for Bitcoin historical data...")
    print("=" * 60)
    
    # Bitcoin ticker
    btc = yf.Ticker("BTC-EUR")
    
    # Get full historical data
    print("\n1. Fetching full Bitcoin historical data (BTC-EUR)...")
    hist = btc.history(period="max")
    
    print(f"✅ Total data points: {len(hist)}")
    print(f"📅 First date: {hist.index[0].strftime('%Y-%m-%d')}")
    print(f"📅 Last date: {hist.index[-1].strftime('%Y-%m-%d')}")
    print(f"💰 First price: €{hist['Close'].iloc[0]:,.2f}")
    print(f"💰 Current price: €{hist['Close'].iloc[-1]:,.2f}")
    
    # Calculate statistics
    prices = hist['Close'].values
    years = (hist.index[-1] - hist.index[0]).days / 365.25
    
    # Calculate returns
    returns = np.diff(np.log(prices))
    
    # Calculate CAGR
    total_return = (prices[-1] / prices[0])
    cagr = (total_return ** (1/years) - 1) * 100
    
    # Calculate volatility (annualized)
    daily_vol = np.std(returns)
    annual_vol = daily_vol * np.sqrt(252) * 100  # 252 trading days
    
    # Calculate Sharpe ratio (assuming 0% risk-free rate)
    mean_daily_return = np.mean(returns)
    sharpe = (mean_daily_return / daily_vol) * np.sqrt(252) if daily_vol > 0 else 0
    
    print(f"\n📊 Statistics ({years:.1f} years):")
    print(f"CAGR: {cagr:.2f}%")
    print(f"Annualized Volatility: {annual_vol:.2f}%")
    print(f"Sharpe Ratio: {sharpe:.2f}")
    print(f"Total Return: {((total_return - 1) * 100):,.0f}%")
    
    # Test monthly resampling for DCA simulation
    print("\n2. Monthly data for DCA simulation:")
    monthly = hist.resample('ME').last()  # Month-end prices
    print(f"Total months: {len(monthly)}")
    print(f"First month: {monthly.index[0].strftime('%Y-%m')}")
    print(f"Last month: {monthly.index[-1].strftime('%Y-%m')}")
    
    # Calculate what €350/month would yield
    dca_amount = 350  # EUR per month
    total_invested = 0
    total_btc = 0
    
    for date, row in monthly.iterrows():
        price = row['Close']
        btc_bought = dca_amount / price
        total_btc += btc_bought
        total_invested += dca_amount
    
    current_value = total_btc * monthly['Close'].iloc[-1]
    roi = ((current_value - total_invested) / total_invested) * 100
    annualized_roi = (pow(current_value / total_invested, 1 / years) - 1) * 100
    
    print(f"\n💰 DCA Strategy (€350/month):")
    print(f"Total Invested: €{total_invested:,.0f}")
    print(f"Total BTC Acquired: {total_btc:.4f} BTC")
    print(f"Current Value: €{current_value:,.0f}")
    print(f"Profit/Loss: €{current_value - total_invested:,.0f}")
    print(f"ROI: {roi:.2f}%")
    print(f"Annualized Return: {annualized_roi:.2f}%")
    
    print("\n" + "=" * 60)
    print("✅ yfinance test complete!")
    
    return hist, monthly

if __name__ == "__main__":
    try:
        hist, monthly = test_bitcoin_data()
    except Exception as e:
        print(f"Error: {e}")
        print("\nTrying to install yfinance...")
        import subprocess
        subprocess.run(["pip3", "install", "yfinance"], check=True)
        hist, monthly = test_bitcoin_data()

