# %%
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import numpy as np

# %% Download TSLA and WMT stock data from Yahoo Finance
tsla = yf.download('TSLA', period='5y', interval='1mo')
wmt = yf.download('WMT', period='5y', interval='1mo')

# %% Calculate the mean and standard deviation of the closing price of TSLA and WMT stock for the past 5 years and put them in one long dataframe
tsla_mean = np.mean(tsla['Adj Close'])
tsla_std = np.std(tsla['Adj Close'])
wmt_mean = np.mean(wmt['Adj Close'])
wmt_std = np.std(wmt['Adj Close'])
long_df = pd.DataFrame({'Stock': ['TSLA', 'WMT'], 'Mean': [tsla_mean, wmt_mean], 'Std': [tsla_std, wmt_std]})
print(long_df)

# %% Plot the monthly closing price of TSLA and WMT stock for the past 5 years
plt.plot(tsla['Adj Close'], label='TSLA')
plt.plot(wmt['Adj Close'], label='WMT')
plt.title('TSLA and WMT Monthly Adj Closing Price (5 Years)')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.show()


# %% Plot the mean vs standard deviation of the closing price of TSLA and WMT stock for the past 5 years
plt.plot(long_df['Std'], long_df['Mean'], 'o')
for i, stock in enumerate(long_df['Stock']):
    plt.annotate(stock, (long_df['Std'][i], long_df['Mean'][i]))
plt.xlabel('Standard Deviation')
plt.ylabel('Mean')
plt.title('Mean vs Standard Deviation of TSLA and WMT')
plt.show()



# %%
