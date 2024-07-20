# Example Strategy Script
import pandas as pd
import sys

# Read the input from stdin
data = pd.read_csv(sys.stdin)

# Calculate the 10-period simple moving average
data['SMA'] = data['Close'].rolling(window=10).mean()

# Generate buy and sell signals
data['signal'] = 0
data.loc[data['Close'] > data['SMA'], 'signal'] = 1  # Buy signal
data.loc[data['Close'] < data['SMA'], 'signal'] = -1  # Sell signal

# Print the results
print(data[['Date','Open', 'Close', 'SMA', 'signal']].tail())