# %% importing packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
import yfinance as yf

# %% Download TSLA data for the past 5 years on a daily basis
tsla_data = yf.download("TSLA", period="5y", interval="1d")

# Print the first 5 rows of the data
print(tsla_data.head())

# %% Plot the closing price of TSLA
# Plot the closing price of TSLA
plt.plot(tsla_data.index, tsla_data['Close'])
plt.title('TSLA Closing Price')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.show()


# %% download housing price index data from Fred with pandas_datareader, from year 2000 to year 2023
import pandas_datareader as pdr

housing_data = pdr.get_data_fred('SPCS20RSA', start=dt.datetime(2000, 1, 1), end=dt.datetime(2023, 1, 1))


print(housing_data.head())

# %% Plot the housing price index data
# Plot the housing price index data
plt.plot(housing_data.index, housing_data['SPCS20RSA'])
plt.title('Housing Price Index')
plt.xlabel('Date')
plt.ylabel('Index')
plt.show()

# %% Plot the housing price index data from year 2012 to year 2014
# Filter the housing price index data for the years 2012 to 2014
filtered_data = housing_data.loc['2012':'2014']

# Plot the filtered housing price index data
plt.plot(filtered_data.index, filtered_data['SPCS20RSA'])
plt.title('Housing Price Index (2012-2014)')
plt.xlabel('Date')
plt.ylabel('Index')
plt.show()



# %% Plot the returns for TSLA
# Calculate the returns for TSLA
tsla_returns = tsla_data['Adj Close'].pct_change()

# Plot the returns for TSLA
plt.plot(tsla_returns)
plt.title('TSLA Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.show()

# %% Plot the returns for Housing price index
# Calculate the returns for Housing price index
housing_returns = housing_data['SPCS20RSA'].pct_change()

# Plot the returns for Housing price index
plt.plot(housing_returns)
plt.title('Housing Price Index Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.show()
# %% plot the filtered housing price index returns
# Filter the housing price index data for the years 2012 to 2014
filtered_data = housing_data.loc['2012':'2014']

# Calculate the returns for the filtered housing price index
filtered_returns = filtered_data['SPCS20RSA'].pct_change()

# Plot the filtered housing price index returns
plt.plot(filtered_returns)
plt.title('Filtered Housing Price Index Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.show()


# %% make the filtered housing price index returns plot more readable. Show only the months
# %% plot the filtered housing price index returns
# Filter the housing price index data for the years 2012 to 2014
filtered_data = housing_data.loc['2012':'2014']

# Calculate the returns for the filtered housing price index
filtered_returns = filtered_data['SPCS20RSA'].pct_change()

# Plot the filtered housing price index returns
plt.plot(filtered_returns)

# Format the x-axis ticks to show only the quarters, not the years
  
plt.gca().xaxis.set_major_locator(mdates.QuarterLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))

plt.title('Filtered Housing Price Index Returns')
plt.xlabel('Date')
plt.ylabel('Returns')
plt.show()

# %% check on seasonality on the filtered housing price index
from statsmodels.tsa.seasonal import seasonal_decompose


# %% Perform seasonal decomposition
filtered_returns = filtered_returns.dropna()
result = seasonal_decompose(filtered_returns, model='additive')

# %% Plot the seasonal component
result.seasonal.plot()
plt.title('Seasonal Component of Filtered Housing Price Index Returns')
plt.xlabel('Date')
plt.ylabel('Seasonal Component')
plt.show()

# %% Plot the trend component
# Perform seasonal decomposition

result = seasonal_decompose(filtered_returns, model='additive')

# Plot the trend component
result.trend.plot()
plt.title('Trend Component of Filtered Housing Price Index Returns')
plt.xlabel('Date')
plt.ylabel('Trend Component')
plt.show()

# %% Plot the residual component
# Plot the residual component
result.resid.plot()
plt.title('Residual Component of Filtered Housing Price Index Returns')
plt.xlabel('Date')
plt.ylabel('Residual Component')
plt.show()

# %% forecast the filtered housing price index returns
# Forecast the filtered housing price index returns
from statsmodels.tsa.arima.model import ARIMA

# Fit the ARIMA model
model = ARIMA(filtered_returns, order=(1, 0, 0))
model_fit = model.fit()

# Forecast the returns
forecast = model_fit.forecast(steps=10)

# %% Plot the forecasted returns with the original returns
# Plot the forecasted returns 
plt.plot(forecast, color='red', label='Forecasted Returns')
plt.plot(filtered_returns, color='blue', label='Original Returns')
plt.title('Forecasted vs Original Returns')
plt.xlabel('Time')
plt.ylabel('Returns')
plt.legend()
plt.show()


# %%
