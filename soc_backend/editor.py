# import pandas as pd
# import numpy as np
# from data_fetch import download_historical_data

# def strategy_build(symbol, start_date, end_date):
#     # Download historical data
#     df = download_historical_data(symbol, start_date, end_date)
    
#     # Calculate 20-day and 9-day SMAs
#     df['sma_20'] = df['Close'].rolling(window=20).mean()
#     df['sma_9'] = df['Close'].rolling(window=9).mean()
    
#     # Initialize signal columns
#     df['signal'] = 0  # 0 for hold
#     df['position'] = np.nan  # NaN for initial position
    
#     # Generate buy signals (9-day SMA crosses above 20-day SMA)
#     df.loc[df['sma_9'] > df['sma_20'], 'signal'] = 1  # 1 for buy
    
#     # Generate sell signals (9-day SMA crosses below 20-day SMA)
#     df.loc[df['sma_9'] < df['sma_20'], 'signal'] = -1  # -1 for sell
    
#     # Forward fill the signal to avoid look-ahead bias
#     df['signal'] = df['signal'].fillna(method='ffill')
    
#     return df



# class TradingExecution:
#     def __init__(self):
#         self.position = 0  # Initial position (0 for neutral, 1 for long, -1 for short)
#         self.trades = []   # List to store trade details
    
#     def run(self, df, symbol, start_date, end_date):
#         returns_series = pd.Series(index=df.index, dtype='float64')  # Specify dtype explicitly  # Series to store returns
        
#         for i in range(1, len(df)):
#             if df['signal'].iloc[i] == 1 and self.position != 1:  # Buy signal and not already long
#                 # Execute buy trade
#                 if self.position == -1:
#                     # Close existing short position
#                     self.close_trade(df, i)
                
#                 # Open new long position
#                 self.position = 1
#                 self.open_trade(df, i)
                
#             elif df['signal'].iloc[i] == -1 and self.position != -1:  # Sell signal and not already short
#                 # Execute sell trade
#                 if self.position == 1:
#                     # Close existing long position
#                     self.close_trade(df, i)
                
#                 # Open new short position
#                 self.position = -1
#                 self.open_trade(df, i)
            
#             # Calculate returns based on close price changes
#             if self.position != 0:
#                 close_price_change = df['Close'].iloc[i] / df['Close'].iloc[i-1] - 1
#                 returns_series.iloc[i] = close_price_change
        
#         return returns_series
    
#     def open_trade(self, df, i):
#         self.trades.append({
#             'type': 'buy' if self.position == 1 else 'sell',
#             'date': df.index[i],
#             'price': df['Close'].iloc[i],
#             'position': self.position
#         })
    
#     def close_trade(self, df, i):
#         # Close trade at current price
#         close_price = df['Close'].iloc[i]
#         trade = self.trades[-1]
#         trade['close_date'] = df.index[i]
#         trade['close_price'] = close_price
        
#         # Calculate returns
#         if trade['position'] == 1:  # Long position
#             trade['returns'] = (close_price / trade['price']) - 1
#         elif trade['position'] == -1:  # Short position
#             trade['returns'] = (trade['price'] / close_price) - 1
        
#         self.position = 0  # Reset position to neutral after closing trade
    

# # Example usage:
# symbol = 'GANESHHOUC.NS'
# start_date = '2024-04-01'
# end_date = '2024-09-01'

# # Step 1: Build strategy
# df_strategy = strategy_build(symbol, start_date, end_date)

# # Step 2: Execute trades based on strategy
# execution = TradingExecution()
# returns = execution.run(df_strategy, symbol, start_date, end_date)

# print("Returns Series:")
# print(returns)

import pandas as pd
import numpy as np
from data_fetch import download_historical_data

def strategy_build(symbol, start_date, end_date):
    df = download_historical_data(symbol, start_date, end_date)
    
    # Calculate 9-day and 20-day SMA
    df['SMA_9'] = df['Close'].rolling(window=9).mean()
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    
    # Generate signals
    df['signal'] = 0
    df.loc[df['SMA_9'] > df['SMA_20'], 'signal'] = 1
    df.loc[df['SMA_9'] < df['SMA_20'], 'signal'] = -1
    
    return df

# class TradingExecution:
#     def __init__(self):
#         pass

#     def execute(self, strategy_code):
#         # Assuming the strategy_code includes the symbol, start_date, and end_date
#         strategy_locals = {}
#         try:
#             exec(strategy_code, globals(), strategy_locals)

#             symbol = strategy_locals['symbol']
#             start_date = strategy_locals['start_date']
#             end_date = strategy_locals['end_date']

#             df = strategy_build(symbol, start_date, end_date)

#             # Initialize position, buy_price, and stop_loss variables
#             position = 0
#             buy_price = 0
#             stop_loss = 0.05  # 5% stop loss level
#             returns = []

#             for i in range(len(df)):
#                 if df['signal'].iloc[i] == 1:  # Buy signal
#                     if position == 0:
#                         position = 1
#                         buy_price = df['Close'].iloc[i]
#                 elif df['signal'].iloc[i] == -1:  # Sell signal
#                     if position == 1:
#                         position = 0
#                         sell_price = df['Close'].iloc[i]
#                         trade_return = (sell_price - buy_price) / buy_price
#                         returns.append(trade_return)
#                 else:  # Hold signal
#                     if position == 1:
#                         current_price = df['Close'].iloc[i]
#                         if (current_price - buy_price) / buy_price <= -stop_loss:
#                             position = 0
#                             trade_return = (current_price - buy_price) / buy_price
#                             returns.append(trade_return)

#             # Convert returns list to a time-indexed Pandas series
#             returns_series = pd.Series(returns, index=df.index[-len(returns):])
            
#             return returns_series.to_dict()
#         except Exception as e:
#             print("Error executing strategy:", e)
#             raise e
