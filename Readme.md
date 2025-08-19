# Quantitative Research Report on Stock Analysis with Case Study on BSE Ltd (BSE-EQ)
<p align="justify">
This project combines equity research with quantitative finance techniques and Python based modeling to simulate and analyze BSE Ltd.'s stock price behavior using historical and derivative market data.
Purpose of this report is to Elevating Traditional Stock Analysis with Advanced Quantitative Methods and Python. This project is created as part of academic blend finance and technology using Python. It demonstrates how financial data can be transformed into actionable insight through simulation and modeling.
</p>

## Contents

- **Fundamentals & Financials** Business, Pe/Pb, Dividend, Comparison 
- **Monte Carlo Simulation** using Geometric Brownian Motion
- **Linear Regression** on EPS vs Stock Price for valuation forecasting
- **Visualization** of price paths, histograms, and technical signals
- **Black-Scholes Model** for European option pricing
- **Technical Analysis**: Chart, EMA (20/50/100), IV, Fibonacchi Levels
- **Derivative Analysis**

## Libraries Used

- `numpy`, `pandas` – numerical & data analysis
- `matplotlib`, `seaborn` – plotting
- `scikit-learn` – regression modeling
- `scipy.stats` – statistical calculations
- `yfinance` – historical data

## Files

- [`BSE_Derivative_data.csv`](https://ishaan145.github.io/Equity-Research/Main/Derivative/Data/BSE_Derivative_data.csv) – main Jupyter Notebook
- [`BSE_Derivative_data.csv`](https://ishaan145.github.io/Equity-Research/Main/Derivative/Data/BSE_Derivative_data.csv) – printable report version
- [`BSE_Derivative_data.csv`](https://ishaan145.github.io/Equity-Research/Main/Derivative/Data/BSE_Derivative_data.csv) – simulated outcome statistics
- [`BSE_Derivative_data.csv`](https://ishaan145.github.io/Equity-Research/Main/Derivative/Data/BSE_Derivative_data.csv) –  [View Option Data](https://ishaan145.github.io/Equity-Research/Main/Derivative/Data/Option_data.html)

## Disclaimer
<p align="justify">
All data used is for educational purposes. No investment advice is provided. This report is intended purely for educational purposes.
All data presented in this report has been sourced from publicly available data as of 08/07/2025, information on the National Stock Exchange of India Ltd (NSE) website: https://www.nseindia.com/get-quotes/equity?symbol=BSE 
</p>
---

**Author**: Ishaan Saxena  
**Release**: You can view the project document by downloading the [**Project Report**](https://ishaan145.github.io/Equity-Research/Main/Derivative/Data/BSE_Derivative_data.pdf).  
**Released On** August 2025

## Overview
<p align="justify">
The primary objective of this report is to demonstrate how a foundational stock analysis, such as the comprehensive research on BSE Ltd. provided, can be significantly enhanced through the integration of advanced quantitative techniques and computational tools, particularly Python. While fundamental and technical analyses offer indispensable insights into a company's intrinsic value and market sentiment, quantitative methods introduce layers of statistical rigor, predictive modeling, and sophisticated risk assessment. These advanced approaches are increasingly vital in navigating the complexities of modern financial markets, providing a more robust and data-driven perspective for investment decisions. This report aims to bridge the gap between conventional financial research and cutting-edge analytical capabilities.
</p>

## Structure
<p align="justify">
This report is structured to provide a comprehensive and integrated assessment of BSE Ltd. It commences with a review of the existing fundamental and technical analyses, building upon the initial research provided. Subsequently, it introduces a layer of quantitative enhancements, detailing how Python-based methodologies can be applied to deepen the understanding of stock behavior and market dynamics. The analytical approach emphasizes the synthesis of observations from all these layers fundamental, technical, and quantitative to deliver a holistic and robust evaluation of BSE Ltd.'s investment profile and future outlook.
</p>

##  Simulation Parameters

S0 = 2376.30      (Current stock price)
mu = 0.12         (Expected annual return)
sigma = 0.45      (Annual volatility)
steps = 252       (Trading days)
T = 17days        (Expiry time for option)
n_simulations = 1000

```

**Key Results:**
- **Mean Ending Price**: ₹2,686.52
- **Median Ending Price**: ₹2,441.62
- **95% Confidence Interval**: ₹1,172.30 - ₹5,171.12

##  Installation & Usage

### Prerequisites
```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy yfinance
```

### Quick Start
```python
# Clone the repository
git clone https://github.com/ishaan145/Equity-Research.git

# Navigate to project directory
cd Equity-Research

# Run the analysis
python Equity_Research.py
```

##  Project Structure

```
BSE-Stock-Analysis/
├──  README.md         
├──  report.html 
├──  bse_analysis.py    
├──  main
│   ├── BSE_Derivative_data.csv
│   └── historical_prices.csv
│   ├── monte_carlo_simulation.png
│   ├── ema_analysis.png
│   └── fibonacci_levels.png
├──  notebooks/
│   └── BSE_Analysis.ipynb
└──  docs/
    └── methodology.md
```


##  Data Sources

- **Primary**: [NSE India](https://www.nseindia.com/get-quotes/equity?symbol=BSE)
- **Historical Data**: Yahoo Finance API
- **Option Chain**: Real-time derivative market data
- **Financial Statements**: Public filings and quarterly reports

---

##  Disclaimer
<p align="justify">
All data used is for educational purposes. No investment advice is provided. This report is intended purely for educational purposes.The quantitative models and simulations presented are based on historical data and mathematical assumptions that may not accurately predict future market behavior. All data presented in this report has been sourced from publicly available data as of July 8, 2025, information on the National Stock Exchange of India Ltd (NSE) website: https://www.nseindia.com/get-quotes/equity?symbol=BSE 
</p>

---

<div align="center">
  <h3>Contact</h3>
  <p>
    <strong>Author:</strong> Ishaan Saxena<br>
    <strong>Release Date:</strong> August 2025<br>
    <strong>Project Type:</strong> Academic Research & Financial Analysis
  </p>
  
  <p>
    <a href="mailto:23mc3027@rfipt.ac.in"> Email</a> |
    <a href="https://linkedin.com/in/ishaansaxena1"> LinkedIn</a> |
    <a href="https://github.com/ishaan145"> GitHub</a>
  </p>
</div>

---


<div align="center">
  <p><strong><a href="https://github.com/Ishaan145/Equity-Research/">You can view the project document by downloading the Project Report</a></strong></p>
   <p><strong><a href="https://ishaan145.github.io/Equity-Research/Main/Derivative/Data/BSE_Derivative_data.pdf">Access Complete Interactive Report Repo</a></strong></p>
</div>

