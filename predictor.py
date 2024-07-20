import pandas as pd 
import matplotlib.pyplot as plt 
import yfinance as yf 
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Mock download_historical_data function (replace this with your actual function)
def download_historical_data(symbol, start_date, end_date, timeframe="1d"):
    get_data = yf.Ticker(symbol)
    df = get_data.history(start=start_date, end=end_date, interval=timeframe)

    # Ensure the data is sorted by date
    df = df.sort_values(by='Date')

    # Calculate daily returns
    df['Daily_Return'] = df['Close'].pct_change() * 100

    # Calculate cumulative returns
    df['Cumulative_Return'] = (df['Close'] / df['Close'].iloc[0] - 1) * 100

    # Drop the first row since it will have NaN for daily return
    df = df.dropna()
    df.reset_index(inplace=True)
    return df 

# Replace with your actual function call
stock_symbol = 'IDEA.NS'
start_date = '2000-01-01'
end_date = '2024-06-06'
data = download_historical_data(stock_symbol, start_date, end_date)

# Check for stationarity
def adf_test(series):
    result = adfuller(series)
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    for key, value in result[4].items():
        print(f'Critical Values {key}: {value}')

# Original series
print("Original Series ADF Test:")
adf_test(data['Close'])

# Differencing
data_diff = data['Close'].diff().dropna()

# Differenced series
print("\nDifferenced Series ADF Test:")
adf_test(data_diff)

# Plot ACF and PACF for the differenced series
plt.figure(figsize=(12, 6))

# ACF plot
plt.subplot(121)
plot_acf(data_diff, ax=plt.gca(), lags=20)
plt.title('Autocorrelation Function')

# PACF plot
plt.subplot(122)
plot_pacf(data_diff, ax=plt.gca(), lags=20)
plt.title('Partial Autocorrelation Function')

plt.tight_layout()
plt.show()

# Determine p, d, q from the plots
# Based on the plots, let's assume p=5 and d=2
p = 0
d = 1
q = 0

# Fit ARIMA model
model = ARIMA(data['Close'], order=(p, d, q))
model_fit = model.fit()

print(model_fit.summary())

# Plot the residual errors
residuals = pd.DataFrame(model_fit.resid)
residuals.plot()
plt.show()
residuals.plot(kind='kde')
plt.show()
print(residuals.describe())

# Forecasting
forecast_steps = 30  # Forecast next 30 days
forecast = model_fit.forecast(steps=forecast_steps)
print(forecast)

# Plot the forecast
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Original')
plt.plot(pd.date_range(start=data.index[-1], periods=forecast_steps, freq='B'), forecast, label='Forecast')
plt.legend()
plt.show()

# import pandas as pd 
# import matplotlib.pyplot as plt 
# import yfinance as yf 
# from pmdarima import auto_arima
# from statsmodels.tsa.stattools import adfuller

# # Mock download_historical_data function (replace this with your actual function)
# def download_historical_data(symbol , start_date , end_date , timeframe = "1d"):

#     get_data = yf.Ticker(symbol)
#     pd.set_option('display.max_columns', None)  # None means unlimited columns will be displayed

#     df = get_data.history(start=start_date,end=end_date, interval = timeframe)

#     # Ensure the data is sorted by date
#     df = df.sort_values(by='Date')

#     # Calculate daily returns
#     df['Daily_Return'] = df['Close'].pct_change() * 100

#     # Calculate cumulative returns
#     df['Cumulative_Return'] = (df['Close'] / df['Close'].iloc[0] - 1) * 100

#     # Drop the first row since it will have NaN for daily return
#     df = df.dropna()
#     df.reset_index(inplace=True)
#     return df 

# # Replace with your actual function call
# stock_symbol = 'IDEA.NS'
# start_date = '2000-01-01'
# end_date = '2024-06-06'
# data = download_historical_data(stock_symbol, start_date, end_date)
# data = data['Close']

# # Check for stationarity with Augmented Dickey-Fuller test
# adf_result = adfuller(data)
# print('ADF Statistic:', adf_result[0])
# print('p-value:', adf_result[1])

# # Use auto_arima to find the optimal p, d, q
# stepwise_model = auto_arima(data, start_p=1, start_q=1,
#                             max_p=5, max_q=5, seasonal=False,
#                             trace=True, error_action='ignore',
#                             suppress_warnings=True, stepwise=True)

# # Fit the ARIMA model with the determined p, d, q
# model = stepwise_model.fit(data)

# # Forecasting
# forecast_steps = 30
# forecast = model.predict(n_periods=forecast_steps)

# # Plot the forecast
# plt.figure(figsize=(14, 7))
# plt.plot(data.index, data, label='Actual')
# plt.plot(data.index[-1] + pd.Timedelta(days=1), data[-1], 'o', label='Last Actual Value', markersize=10)
# plt.plot(pd.date_range(start=data.index[-1], periods=forecast_steps + 1, closed='right'), [data[-1]] + list(forecast), label='Forecast')
# plt.title(f'{stock_symbol} Stock Price Forecast')
# plt.xlabel('Date')
# plt.ylabel('Stock Price')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()
