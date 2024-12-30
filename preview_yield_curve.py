import pandas_datareader as pdr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

# Get Treasury rates data from FRED starting from 1976
start_date = '1976-01-01'
rates = pd.DataFrame()
rates['10YR'] = pdr.get_data_fred('DGS10', start=start_date)  # 10-year rate
rates['2YR'] = pdr.get_data_fred('DGS2', start=start_date)    # 2-year rate
rates['Spread'] = rates['10YR'] - rates['2YR']  # Yield curve spread

# Get recession data
recession = pdr.get_data_fred('USREC', start=start_date)

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12), height_ratios=[2, 1])

# Plot 1: Treasury Rates
ax1.plot(rates.index, rates['10YR'], 'b-', label='10-Year Treasury', linewidth=2)
ax1.plot(rates.index, rates['2YR'], 'r-', label='2-Year Treasury', linewidth=2)

# Highlight recession periods in both plots
for i in range(len(recession)-1):
    if recession['USREC'].iloc[i] == 1:
        ax1.axvspan(recession.index[i], recession.index[i+1], 
                   color='gray', alpha=0.2)
        ax2.axvspan(recession.index[i], recession.index[i+1], 
                   color='gray', alpha=0.2)

ax1.set_title('Historical Treasury Rates: 10-Year vs 2-Year (1976-Present)', fontsize=14)
ax1.set_ylabel('Yield (%)', fontsize=12)
ax1.grid(True)
ax1.legend(fontsize=12)
ax1.tick_params(axis='both', which='major', labelsize=10)

# Plot 2: Yield Curve Spread
ax2.plot(rates.index, rates['Spread'], 'g-', label='10Y-2Y Spread', linewidth=2)
ax2.axhline(y=0, color='r', linestyle='--', alpha=0.5)  # Add zero line
ax2.fill_between(rates.index, rates['Spread'], 0, 
                 where=(rates['Spread'] < 0),
                 color='r', alpha=0.3,
                 label='Yield Curve Inversion')

# Add annotations for notable events
events = {
    '1980-01-01': 'Volcker\nRecession',
    '1990-07-01': '90s\nRecession',
    '2001-03-01': 'Dot-Com\nBurst',
    '2008-09-15': 'Financial\nCrisis',
    '2020-03-01': 'COVID-19'
}

for date, label in events.items():
    event_date = pd.to_datetime(date)
    if event_date in rates.index:
        ax1.annotate(label, 
                    xy=(event_date, ax1.get_ylim()[1]),
                    xytext=(10, 10), textcoords='offset points',
                    fontsize=10,
                    bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.3),
                    rotation=0)

ax2.set_title('Yield Curve Spread (10Y-2Y) with Recession Indicators', fontsize=14)
ax2.set_ylabel('Spread (%)', fontsize=12)
ax2.grid(True)
ax2.legend(fontsize=12)
ax2.tick_params(axis='both', which='major', labelsize=10)

# Add text box explaining the relationship
text = ("Yield Curve Inversion (red areas) occurs when\n"
        "the 2-year rate exceeds the 10-year rate.\n"
        "This has historically preceded recessions (gray areas).")
plt.figtext(0.15, 0.02, text, fontsize=12, 
            bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()

# Current yield curve shape
maturities = ['1MO', '3MO', '6MO', '1YR', '2YR', '5YR', '10YR', '30YR']
tickers = ['DGS1MO', 'DGS3MO', 'DGS6MO', 'DGS1', 'DGS2', 'DGS5', 'DGS10', 'DGS30']
current_rates = pd.DataFrame()

for ticker in tickers:
    current_rates[ticker] = pdr.get_data_fred(ticker)

# Plot current yield curve
plt.figure(figsize=(12, 8))
plt.plot(range(len(maturities)), current_rates.iloc[-1], 'bo-', linewidth=2, markersize=10)

# Add labels
plt.title('Current Treasury Yield Curve Shape', fontsize=14)
plt.xlabel('Maturity', fontsize=12)
plt.ylabel('Yield (%)', fontsize=12)
plt.xticks(range(len(maturities)), maturities, rotation=45)
plt.grid(True)

# Add annotation about curve shape
if current_rates.iloc[-1]['DGS2'] > current_rates.iloc[-1]['DGS10']:
    plt.text(0.6, 0.9, 'Inverted Yield Curve\n(Potential Recession Signal)', 
             transform=plt.gca().transAxes, 
             bbox=dict(facecolor='red', alpha=0.2),
             fontsize=12)
else:
    plt.text(0.6, 0.9, 'Normal Yield Curve', 
             transform=plt.gca().transAxes, 
             bbox=dict(facecolor='green', alpha=0.2),
             fontsize=12)

plt.legend(['Current Yield Curve'], fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.tight_layout()
plt.show()
