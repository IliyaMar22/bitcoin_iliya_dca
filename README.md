# 🪙 Bitcoin DCA Monte Carlo Simulator

A sophisticated Monte Carlo simulation tool to analyze Dollar Cost Averaging (DCA) strategy for Bitcoin investments.

## 📊 What It Does

Simulates the performance of investing **€350/month** into Bitcoin over different time horizons (3, 5, and 10 years) using real historical statistics and Monte Carlo methods.

## 🎯 Key Features

### Real Bitcoin Statistics
- **CAGR**: 99.05% (13-year historical data)
- **Volatility**: 149.87% (annualized)
- **Sharpe Ratio**: 0.82
- Based on actual Bitcoin price history from 2012-2025

### Analysis Capabilities
- **10,000+ simulations** per time period
- Distribution of potential outcomes
- Percentile analysis (5th, 25th, 50th, 75th, 95th)
- ROI and annualized return calculations
- Break-even probability
- Visual histograms and charts

### Investment Strategy
- Fixed monthly investment: €350/month
- Dollar Cost Averaging (DCA) approach
- Automatic price fetching from CoinGecko API
- Historical data-driven simulations

## 🚀 Quick Start

### Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

### Python Testing

```bash
cd ..
pip3 install yfinance pandas numpy
python3 test_yfinance.py
```

## 📈 What You'll Learn

1. **Potential Returns**: Distribution of possible outcomes
2. **Risk Assessment**: Best case (95th) vs worst case (5th percentile)
3. **Break-Even Probability**: Chance of positive returns
4. **DCA Benefits**: How consistent investing smooths volatility

## 🎨 Technology Stack

- **Frontend**: Next.js 14, React, TypeScript
- **Charts**: Recharts
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **Data Source**: CoinGecko API, yfinance

## 📊 Example Results (Historical)

If you had DCA'd €350/month since 2014:
- **Total Invested**: €46,900
- **BTC Acquired**: ~35.5 BTC
- **Current Value**: ~€3.8M
- **ROI**: ~8,000%

*Past performance doesn't guarantee future results!*

## 🔧 Configuration

The simulator uses real Bitcoin statistics:
- Historical CAGR: 99.05%
- Historical Volatility: 149.87%
- Monthly investment: €350 (configurable in code)
- Simulation count: 10,000 (configurable in UI)

## ⚠️ Disclaimer

This tool is for **educational and research purposes only**. 

- Bitcoin is extremely volatile
- Past performance doesn't predict future results
- Only invest what you can afford to lose
- Cryptocurrency investments carry significant risk
- This is NOT financial advice

## 📝 API Keys

- **CoinGecko API**: Uses demo key for current prices
- **yfinance**: No API key required for historical data

## 🚀 Deployment

### Deploy to Vercel

```bash
cd frontend
vercel --prod
```

Or connect your GitHub repository to Vercel for automatic deployments.

## 🧪 Testing

Test the data sources:

```bash
# Test CoinGecko API
python3 test_coingecko.py

# Test yfinance (full historical data)
python3 test_yfinance.py
```

## 📊 Monte Carlo Methodology

1. **Historical Analysis**: Calculate mean returns and volatility from real data
2. **Random Walk**: Generate price paths using log-normal distribution
3. **DCA Simulation**: Apply €350/month purchases at simulated prices
4. **Statistical Analysis**: Calculate percentiles, ROI, and probabilities
5. **Visualization**: Display results with interactive charts

## 🤝 Contributing

This is an educational project. Feel free to fork and modify for your own analysis!

## 📄 License

MIT License - Use freely for educational purposes

---

**Remember**: Cryptocurrency investments are highly speculative. This tool helps you understand potential outcomes but cannot predict the future. Always do your own research and consult with financial advisors before making investment decisions.

