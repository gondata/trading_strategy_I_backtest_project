# Trading Strategy Backtest for Bank of America (BAC) Stock

This code implements a simple trading strategy using moving averages for Bank of America (BAC) stock. It includes a backtest and visualizations of the results.

## Requirements

- numpy
- pandas
- matplotlib
- seaborn
- yfinance
- pandas-datareader

## Instructions

1. Install the required packages: `pip install -r requirements.txt`
2. Run the code in a Jupyter Notebook or Python environment.
3. The code will fetch the BAC stock data from Yahoo Finance and calculate the moving averages.
4. Three graphs will be generated to show the trading strategy, backtest, and returns distribution.

## Strategy

1. Create a DataFrame with dates and calculate the moving averages.
2. Generate signals based on when the short moving average is greater than the long moving average.
3. Create a DataFrame with positions based on the signals.
4. Backtest the strategy by calculating the returns and portfolio value.

## Graphs

1. Trading strategy: shows the stock price, short and long moving averages, and buy/sell signals.
2. Backtest: shows the portfolio value and buy/sell signals.
3. Returns distribution: shows the distribution of the returns.
