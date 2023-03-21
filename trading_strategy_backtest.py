# Importing the libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

# Getting the data

assets = ['BAC']
startdate = '2020-01-01'
enddate = '2023-03-12'

data = pdr.get_data_yahoo(assets, start=startdate, end=enddate)['Adj Close']

# Variables

short_window = 50
long_window = 150

# Strategy

signal = pd.DataFrame(index=data.index) # Creating a DataFrame with dates
signal['short'] = data.rolling(short_window).mean()
signal['long'] = data.rolling(long_window).mean()

signal['signals'] = np.where(signal['short'] > signal['long'], 1, 0)

signal['positions'] = signal['signals'].diff()

# Graph 1

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(121, ylabel=assets)
ax1.set_title(str(assets) + " Trading strategy")
data.iloc[long_window:].plot(ax=ax1, color='k', lw=1.9)
signal[['short', 'long']].plot(ax=ax1, lw=1.3)
ax1.plot(signal['short'][signal['positions'] == 1], '^', markersize=8, color='g')
ax1.plot(signal['short'][signal['positions'] == -1], 'v', markersize=8, color='r')


# Backtest

capital = int(100000)
stocks = int(300)

positions = pd.DataFrame(index=signal.index)
positions['BAC'] = stocks*signal['signals']

portfolio = pd.DataFrame(data=positions['BAC'].multiply(data), columns=['BAC'])

pos_diff = positions['BAC'].diff()

portfolio['Portfolio'] = portfolio
portfolio['Cash'] = capital - (pos_diff.multiply(data).cumsum())
portfolio['Total'] = portfolio['Cash'] + portfolio['Portfolio']
portfolio['Returns'] = portfolio['Total'].pct_change()[1:]

portfolio['Returns'] = portfolio['Returns'][portfolio['Returns'] != 0]

# Graph 2

ax2 = fig.add_subplot(222, ylabel='Portfolio value')
portfolio['Total'].plot(ax=ax2, lw=2, label='Portfolio Total')
ax2.plot(portfolio['Total'][signal['positions'] == 1], '^', markersize=8, color='g')
ax2.plot(portfolio['Total'][signal['positions'] == -1], 'v', markersize=8, color='r')

# Graph 3

ax3= fig.add_subplot(224)
sns.histplot(portfolio['Returns'], kde=True, ax=ax3)
plt.show()