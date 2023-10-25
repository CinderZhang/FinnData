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
# General idea of ARIMA: https://docs.google.com/document/d/1zpFHGSBd5pZzAyZg1In5YNlHGRRl5UUIRlQeULBE4mk/edit?usp=sharing
model = ARIMA(filtered_returns, order=(5, 0, 0))
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


# %% download WMT 10 years of quarterly revenue and ebitda data from yahoo finance
from yahoofinancials import YahooFinancials
import pandas as pd
ticker = 'AAPL'
yahoo_financials = YahooFinancials(ticker)
eps = yahoo_financials.get_earnings_per_share()

# %% more information about AAPL
# balance_sheet_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'balance')
# income_statement_data_qt = yahoo_financials.get_financial_stmts('quarterly', 'income')
all_statement_data_qt =  yahoo_financials.get_financial_stmts('quarterly', ['income', 'cash', 'balance'])
# apple_earnings_data = yahoo_financials.get_stock_earnings_data()
# apple_net_income = yahoo_financials.get_net_income()
# historical_stock_prices = yahoo_financials.get_historical_price_data('2008-09-15', '2018-09-15', 'weekly')
# %% save the dictionary to a json file
import json
with open('financialstatements.json', 'w') as fp:
    json.dump(all_statement_data_qt, fp)
    

# %% read the json file and extract net incomes
import json
import pandas as pd

# Initialize empty lists to store the net income and corresponding dates
net_income_common_stockholders = []
net_income = []
dates = []

# Read the uploaded JSON file
file_path = 'financialstatements.json'  # Replace with the path to your JSON file
with open(file_path, 'r') as f:
    financial_data = json.load(f)

# Extract the net income and dates
try:
    for company, statements in financial_data['incomeStatementHistoryQuarterly'].items():
        for statement in statements:
            for date, metrics in statement.items():
                dates.append(date)
                net_income_common_stockholders.append(metrics.get('netIncomeCommonStockholders', None))
                net_income.append(metrics.get('netIncome', None))
except KeyError as e:
    print(f"KeyError: {e} not found in the data")

# Combine extracted data into a DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Net Income (Common Stockholders)': net_income_common_stockholders,
    'Net Income': net_income
})

# Show the DataFrame (you can also save it to a CSV or any other format)
print(df)



# %%
