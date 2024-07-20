import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from data_fetch import download_historical_data




def calculate_sharpe_ratio(returns, risk_free_rate=0):
    excess_returns = returns - risk_free_rate
    return np.sqrt(252) * (excess_returns.mean() / excess_returns.std())

def calculate_sortino_ratio(returns, risk_free_rate=0):
    excess_returns = returns - risk_free_rate
    downside_deviation = np.sqrt(np.mean(np.square(np.clip(excess_returns, None, 0))))
    return np.sqrt(252) * (excess_returns.mean() / downside_deviation)

def calculate_maximum_drawdown(returns):
    cumulative_returns = (1 + returns).cumprod()
    running_max = cumulative_returns.cummax()
    drawdown = (cumulative_returns - running_max) / running_max
    max_drawdown = drawdown.min()
    return max_drawdown

def calculate_monthly_returns(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df['Monthly_Return'] = df['Close'].resample('M').ffill().pct_change()
    return df

def calculate_rsi(df, period=14):
    delta = df['Close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period, min_periods=1).mean()
    avg_loss = loss.rolling(window=period, min_periods=1).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def post_trade_analysis(symbol, start_date, end_date):
    df = download_historical_data(symbol, start_date, end_date)
    df['returns'] = df['Close'].pct_change().dropna()
    returns = df['returns']
    
    sharpe_ratio = calculate_sharpe_ratio(returns)
    sortino_ratio = calculate_sortino_ratio(returns)
    max_drawdown = calculate_maximum_drawdown(returns)
    
    # Add results to the DataFrame for visualization
    df['cumulative_returns'] = (1 + returns).cumprod()
    df['sharpe_ratio'] = sharpe_ratio
    df['sortino_ratio'] = sortino_ratio
    df['max_drawdown'] = max_drawdown
    df['RSI'] = calculate_rsi(df)

    # Calculate monthly returns for heatmap
    df = calculate_monthly_returns(df)
    df = df.dropna()
    df.reset_index(inplace=True)

    return df