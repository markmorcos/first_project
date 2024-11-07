# Stock Market Analysis

# Introduction
This project aims to analyze the stock price data of both financial and technological companies, offering a deeper understanding of price volatility and changes over time for begginers in trading. By examining the price movements during major economic events, such as the Covid-19 pandemic and interest rate changes, the project seeks to uncover the factors that influence stock price fluctuations.

The analysis focuses on understanding how different industries respond to economic shifts, comparing the volatility of technology companies with financial firms.

**Hypothesis 1**:
The stock prices of technology companies are more volatile than those of financial companies, leading to larger price swings over time.

**Hypothesis 2**:
Major economic events, such as interest rate changes or inflation reports, lead to significant fluctuations in stock price.

Through this exploration, the project aims to provide valuable insights into the dynamics of stock prices, offering a clearer picture of how external factors drive market behavior in different sectors.

# Installation

<details>
  <summary>Click to see the list of functions</summary>
1. **Clone the repository**:

```bash
git clone https://github.com/YourUsername/repository_name.git
```

2. **Install UV**

If you're a MacOS/Linux user type:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If you're a Windows user open an Anaconda Powershell Prompt and type :

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

3. **Create an environment**

```bash
uv venv 
```

3. **Activate the environment**

If you're a MacOS/Linux user type (if you're using a bash shell):

```bash
source ./venv/bin/activate
```

If you're a MacOS/Linux user type (if you're using a csh/tcsh shell):

```bash
source ./venv/bin/activate.csh
```

If you're a Windows user type:

```bash
.\venv\Scripts\activate
```

4. **Install dependencies**:

```bash
uv pip install -r requirements.txt
```

## Required packages
Pandas, Numpy, Seaborn, Matplotlib.pyplo, plotly.express, plotly.graph_objects, yfinance 

</details>

# Dataset 
Yahoo Finance API was used as main data source, supplemented by additional research on datasets from Kaggle to enrich analysis. All datasets consist of financial statements and are often used to model company valuations and performance.

## Main dataset issues

- Data sourced from different resuorces
- Required formatting and cleaning for consistency.
- Some entries needed adjustments for proper structure.

## Solutions for the dataset issues

The data was standardized, cleaned, and transformed to ensure consistency across sources and to fit the required formatting in order to use same functions

# Questions

- Are stock prices of technology companies more volatile than those of financial companies, leading to larger price swings over time?
- Do major economic events, such as interest rate changes or inflation reports, lead to significant fluctuations in stock price?


# Methodology

The analysis used stock price data from November 2019 onwards, focusing on daily, monthly, and annual trends. Data was cleaned by standardizing dates, aligning column names, and handling missing values. Then the data was analysed for trends, volatility, and patterns over time, using statistical measures such as mean and standard deviation. 

Finally, the data was visualised using charts to highlight important trends and anomalies, ultimately generating insights into the stock's performance over the 5-year period.

# Conclusion

## Hypothesis 1

Based on the reserach, there is no evidence to support that technology companies experience larger price swings or more volatility than financial companies. The price behaviors of both sectors are similar in terms of both average returns and variability during the period under consideration.

## Hypothesis 2

One of the key findings from the analysis was that volume raised exponentially during periods of high uncertainty, particularly during the onset of the Covid-19 pandemic and in response to significant interest rate decisions. This surge in trading volume aligns with increased market volatility and can be attributed to heightened investor fear and speculation.

In conclusion, this analysis confirms the hypothesis 2, and also highlights the complex interplay between economic events, and market volatility.

# Further questions

How do different types of economic events (e.g., inflation, geopolitical crises, technological disruptions) affect volatility in the tech sector compared to other sectors?

Does the observed similarity in volatility across sectors hold true across different time frames(e.g long term period 10,20,30 years)?

# Links to data sources and Trello

## Slides

https://docs.google.com/presentation/d/1pIAcE5RoUORcY9Z3HZl6_fNK113R7y5pWrNVE4h4qxY/edit?usp=sharing

## Trello

https://trello.com/b/hyu8KwSF/stock-market-analysis

## Data sources


https://finance.yahoo.com/quote/NVDA/
https://finance.yahoo.com/quote/MSFT/
https://finance.yahoo.com/quote/GOOG/
https://finance.yahoo.com/quote/AMZN/
https://finance.yahoo.com/quote/NFLX/
https://finance.yahoo.com/quote/AAPL/
https://finance.yahoo.com/quote/META/
https://finance.yahoo.com/quote/UBS/
https://finance.yahoo.com/quote/GS/
https://finance.yahoo.com/quote/JPM/
https://finance.yahoo.com/quote/USB/
