# Basic Time Series Analysis with Financial Data

## Preliminary Task: Draft Your Evaluation Prompt

### Goal

- Prepare for the evaluation of your final work.

### Task

- Draft a prompt that outlines the key points and questions you would like ChatGPT to evaluate in your final work. This will help in assessing the quality and depth of your analysis. ChatGPT should give your a grade for this assignment.

---



---

## Task 1: Introduction to Time Series and Financial Data

### Goal

- Understand what time series data is and how it is relevant in the financial sector.

### Python Task

- Research and write Python comments in a VS Code file summarizing what time series data is and its applications in finance.

### Hint

- Look into the definition of time series data and its importance in financial analysis.

---

## Task 2: Data Collection and Importing from Yahoo Finance

### Goal

- Learn how to collect and import financial time series data.

### Data Source

- Yahoo Finance

### Python Task

- Use Python libraries like `yfinance` to collect stock price data for a company of your choice from Yahoo Finance. Import the data into a Python file in VS Code.

### Hint

- Use the `yfinance` library to fetch data. The function `yf.download('AAPL')` can be used to download Apple's stock data, for example.

---

## Task 3: Data Visualization

### Goal

- Visualize the collected time series data.

### Python Task

- Use Python libraries like `matplotlib` or `seaborn` to create line plots, candlestick charts, and other visualizations for the collected data.

### Hint

- Use `plt.plot()` for line plots and `sns.candlestick_ohlc()` for candlestick charts.

---

## Task 4: Data Manipulation with Returns and Lagged Returns

### Goal

- Learn how to manipulate time series data and generate returns and lagged returns.

### Python Task

- Perform tasks like resampling, calculating moving averages, and handling missing values. Generate returns and 5 lagged returns on the collected data.

### Hint

- Use `df.pct_change()` to calculate returns. For lagged returns, you can use `df['Lagged_Return'] = df['Return'].shift()`.

---

## Task 5: Understanding Seasonality with Housing Price Data

### Goal

- Understand the concept of seasonality in time series data.

### Data Source

- [Freddie Mac House Price Index](http://www.freddiemac.com/research/indices/house-price-index.page)

### Python Task

- Use the Freddie Mac House Price Index data to analyze seasonality in housing prices.

### Hint

- Use `seasonal_decompose` from `statsmodels.tsa.seasonal` to decompose the time series into trend, seasonal, and residual components.

---

## Task 6: Machine Learning Projections with Implications

### Goal

- Use a simple machine learning model to make projections using lagged returns and think about the implications.

### Python Task

- Implement a machine learning model like Linear Regression using libraries like `scikit-learn` to forecast future returns based on the 5 lagged returns you've generated. Reflect on the implications of your analysis and how it connects to any financial knowledge you may have.

### Hint

- Use `LinearRegression()` from `sklearn.linear_model` and fit the model using `.fit(X, y)`, where `X` is the matrix of lagged returns and `y` is the return.

