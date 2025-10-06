# 🚀 Bitcoin DCA Simulator - Deployment Guide

## Quick Deploy to Vercel

### Option 1: GitHub Integration (Recommended)

1. **Create GitHub Repository**:
   ```bash
   # Go to https://github.com/new
   # Create repository named: bitcoin_dca
   # Don't initialize with README
   ```

2. **Push Code**:
   ```bash
   cd bitcoin-dca-simulation
   git remote add origin https://github.com/YOUR_USERNAME/bitcoin_dca.git
   git branch -M main
   git push -u origin main
   ```

3. **Deploy on Vercel**:
   - Go to https://vercel.com
   - Click "New Project"
   - Import your GitHub repository
   - Root Directory: `frontend`
   - Framework Preset: Next.js
   - Click "Deploy"

### Option 2: Vercel CLI

```bash
cd frontend
npm install -g vercel
vercel login
vercel --prod
```

## Configuration

The project is pre-configured with:
- ✅ Next.js 14
- ✅ TypeScript
- ✅ Tailwind CSS
- ✅ Recharts for visualizations
- ✅ CoinGecko API integration
- ✅ Responsive design

## Environment Variables

No environment variables needed! The CoinGecko API key is already integrated.

## Build Settings (if manual configuration needed)

- **Framework Preset**: Next.js
- **Root Directory**: `frontend`
- **Build Command**: `npm run build`
- **Output Directory**: `.next`
- **Install Command**: `npm install`
- **Node Version**: 18.x or higher

## Post-Deployment

After deployment, your simulator will be available at:
`https://your-project-name.vercel.app`

## Features Live:

✅ Bitcoin price fetching from CoinGecko  
✅ 10,000 Monte Carlo simulations  
✅ Interactive charts and visualizations  
✅ 3, 5, and 10 year projections  
✅ Real-time statistics based on 13-year historical data  

## Troubleshooting

### Build Fails
```bash
cd frontend
npm install
npm run build
```

### API Issues
- CoinGecko API is integrated with demo key
- Falls back to synthetic data if API fails
- No API limits for basic price fetching

## Testing Locally

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:3000

## Updates

To update the live site:
```bash
git add .
git commit -m "Update message"
git push origin main
```

Vercel will automatically rebuild and deploy!

---

Need help? Check the main README.md for more details.

