import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# Magnificent 7 stocks
mag7 = {
    'AAPL': 'Apple',
    'MSFT': 'Microsoft',
    'GOOGL': 'Google',
    'AMZN': 'Amazon',
    'NVDA': 'Nvidia',
    'META': 'Meta',
    'TSLA': 'Tesla'
}

# Get data for last 3 months
end_date = datetime.now()
start_date = end_date - timedelta(days=90)

print("Fetching Mag 7 stock data...")

# Download data
data = yf.download(list(mag7.keys()), start=start_date, end=end_date)['Close']

# Calculate percentage change from start (normalized to 100)
normalized = (data / data.iloc[0]) * 100

# Create the chart
plt.figure(figsize=(14, 8))
plt.style.use('seaborn-v0_8-darkgrid')

colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8']

for i, (ticker, name) in enumerate(mag7.items()):
    plt.plot(normalized.index, normalized[ticker], label=f'{name} ({ticker})',
             linewidth=2.5, color=colors[i])

plt.title('Magnificent 7 Stock Performance (Last 3 Months)', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Normalized Price (Start = 100)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, alpha=0.3)

# Add horizontal line at 100 (starting point)
plt.axhline(y=100, color='gray', linestyle='--', alpha=0.5, label='Starting Point')

# Rotate x-axis labels
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart
plt.savefig('/Users/elchinsuleymanov/Documents/Claude-Code/mag7-chart/mag7_performance.png', dpi=150)
print("\nChart saved to mag7-chart/mag7_performance.png")

# Print summary stats
print("\n" + "="*60)
print("PERFORMANCE SUMMARY (Last 3 Months)")
print("="*60)

returns = ((data.iloc[-1] - data.iloc[0]) / data.iloc[0] * 100).round(2)
returns_sorted = returns.sort_values(ascending=False)

for ticker in returns_sorted.index:
    name = mag7[ticker]
    ret = returns_sorted[ticker]
    symbol = "📈" if ret > 0 else "📉"
    print(f"{symbol} {name:12} ({ticker}): {ret:+.2f}%")

print("="*60)

# Show the plot
plt.show()
