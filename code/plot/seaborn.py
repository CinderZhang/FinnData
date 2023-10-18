import yfinance as yf
import seaborn as sns
# import matplotlib.pyplot as plt
# Download TSLA data for the past 5 years on a monthly basis
tsla_data = yf.download("TSLA", period="5y", interval="1mo")

# Print the first 5 rows of the data
print(tsla_data.head())



# Plot TSLA data using seaborn's lineplot function
sns.lineplot(data=tsla_data, x="Date", y="Close")

# Show the plot
plt.show()

