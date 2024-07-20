# import pandas as pd
# import numpy as np
# from statsmodels.tsa.arima.model import ARIMA
# from statsmodels.tsa.stattools import adfuller, acf, pacf
# from statsmodels.tsa.seasonal import seasonal_decompose
# from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
# import matplotlib.pyplot as plt
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# from data_fetch import download_historical_data
# # Define start and end dates
# start_date = "2005-01-01"
# end_date = "2024-07-20"
# symbol = 'GANESHHOUC.NS'

# # Download historical data
# data = download_historical_data(symbol, start_date, end_date)
# data = data.sort_index()
# prices = data['Close']

# # Step 1: Determine differencing order (d) using ADF test
# def adf_test(timeseries):
#     result = adfuller(timeseries)
#     print('ADF Statistic:', result[0])
#     print('p-value:', result[1])
#     for key, value in result[4].items():
#         print('Critical Values:')
#         print(f'   {key}, {value}')
#     return result[1]

# # Initial ADF test
# p_value = adf_test(prices)
# d = 0
# while p_value > 0.05:
#     d += 1
#     prices = prices.diff().dropna()
#     p_value = adf_test(prices)

# print(f'Determined differencing order (d): {d}')

# # Step 2: Check for seasonality
# result = seasonal_decompose(data['Close'], model='multiplicative', period=30)
# result.plot()
# plt.show()

# # Step 3: Plot ACF and PACF to determine p and q
# plt.figure(figsize=(12, 6))

# plt.subplot(211)
# plot_acf(prices, ax=plt.gca(), lags=20)
# plt.title('Autocorrelation Function')

# plt.subplot(212)
# plot_pacf(prices, ax=plt.gca(), lags=20)
# plt.title('Partial Autocorrelation Function')

# plt.tight_layout()
# plt.show()

# # Step 4: Use ACF and PACF plots to determine p and q
# def determine_p_q(prices):
#     lag_acf = acf(prices, nlags=20)
#     lag_pacf = pacf(prices, nlags=20, method='ols')

#     q = np.where(lag_acf < 1.96/np.sqrt(len(prices)))[0][0] if np.any(lag_acf < 1.96/np.sqrt(len(prices))) else 0
#     p = np.where(lag_pacf < 1.96/np.sqrt(len(prices)))[0][0] if np.any(lag_pacf < 1.96/np.sqrt(len(prices))) else 0

#     return p, q

# p, q = determine_p_q(prices)
# print(f'Determined AR order (p): {p}')
# print(f'Determined MA order (q): {q}')

# # Step 5: Fit ARIMA model with determined p, d, q
# model = ARIMA(data['Close'], order=(p, d, q))
# model_fit = model.fit()

# # Print model summary
# print(model_fit.summary())

# # Step 6: Evaluate model accuracy
# train_size = int(len(data) * 0.8)
# train, test = data['Close'][:train_size], data['Close'][train_size:]

# # Fit model on training data
# model = ARIMA(train, order=(p, d, q))
# model_fit = model.fit()

# # Make predictions
# predictions = model_fit.forecast(steps=len(test))

# # Calculate evaluation metrics
# mae = mean_absolute_error(test, predictions)
# mse = mean_squared_error(test, predictions)
# rmse = np.sqrt(mse)
# r2 = r2_score(test, predictions)
# mape = np.mean(np.abs((test - predictions) / test)) * 100

# print(f"Mean Absolute Error (MAE): {mae}")
# print(f"Mean Squared Error (MSE): {mse}")
# print(f"Root Mean Squared Error (RMSE): {rmse}")
# print(f"R-squared (R²): {r2}")
# print(f"Mean Absolute Percentage Error (MAPE): {mape}")

# # Plot observed vs predicted prices
# plt.figure(figsize=(10, 6))
# plt.plot(data['Close'], label='Observed')
# plt.plot(test.index, predictions, label='Predicted', color='red')
# plt.legend()
# plt.show()

# # Step 7: Make future forecasts
# future_forecast = model_fit.forecast(steps=5)
# print(future_forecast)

# # Plot the forecast
# plt.figure(figsize=(10, 6))
# plt.plot(data['Close'], label='Observed')
# plt.plot(future_forecast.index, future_forecast, label='Forecast', color='red')
# plt.legend()
# plt.show()



# import pandas as pd
# import numpy as np
# import statsmodels.api as sm
# from statsmodels.tsa.arima.model import ARIMA
# from statsmodels.tsa.stattools import adfuller, acf, pacf
# import matplotlib.pyplot as plt
# from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# # Load data

# from data_fetch import download_historical_data
# # Define start and end dates
# start_date = "2005-01-01"
# end_date = "2024-07-20"
# symbol = 'GANESHHOUC.NS'

# # Download historical data
# data = download_historical_data(symbol, start_date, end_date)
# data = data.sort_index()
# prices = data['Close']
# # Step 1: Determine differencing order (d) using ADF test
# def adf_test(timeseries):
#     result = adfuller(timeseries)
#     print('ADF Statistic:', result[0])
#     print('p-value:', result[1])
#     for key, value in result[4].items():
#         print('Critical Values:')
#         print(f'   {key}, {value}')
#     return result[1]

# # Initial ADF test
# p_value = adf_test(prices)
# d = 0
# while p_value > 0.05:
#     d += 1
#     prices = prices.diff().dropna()
#     p_value = adf_test(prices)

# print(f'Determined differencing order (d): {d}')

# # Step 2: Plot ACF and PACF to determine p and q
# plt.figure(figsize=(12,6))

# plt.subplot(211)
# plot_acf(prices, ax=plt.gca(), lags=20)
# plt.title('Autocorrelation Function')

# plt.subplot(212)
# plot_pacf(prices, ax=plt.gca(), lags=20)
# plt.title('Partial Autocorrelation Function')

# plt.tight_layout()
# plt.show()

# # Step 3: Use ACF and PACF plots to determine p and q
# # This step requires visual inspection, but we can provide guidance on typical interpretation.

# def determine_p_q(prices):
#     # This is a heuristic method and might not be perfect
#     lag_acf = acf(prices, nlags=20)
#     lag_pacf = pacf(prices, nlags=20, method='ols')

#     # Determine q (cutoff point in ACF)
#     q = np.where(lag_acf < 1.96/np.sqrt(len(prices)))[0][0] if np.any(lag_acf < 1.96/np.sqrt(len(prices))) else 0

#     # Determine p (cutoff point in PACF)
#     p = np.where(lag_pacf < 1.96/np.sqrt(len(prices)))[0][0] if np.any(lag_pacf < 1.96/np.sqrt(len(prices))) else 0

#     return p, q

# p, q = determine_p_q(prices)
# print(f'Determined AR order (p): {p}')
# print(f'Determined MA order (q): {q}')

# # Step 4: Fit ARIMA model with determined p, d, q
# model = ARIMA(data['Close'], order=(p, d, q))
# model_fit = model.fit()

# # Print model summary
# print(model_fit.summary())

# # Make forecast
# forecast = model_fit.forecast(steps=10)
# print(forecast)

# # Plot the forecast
# plt.figure(figsize=(10,6))
# plt.plot(data['Close'], label='Observed')
# plt.plot(forecast, label='Forecast', color='red')
# plt.legend()
# plt.show()

import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller, acf, pacf
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from data_fetch import download_historical_data

def adf_test(timeseries):
    result = adfuller(timeseries)
    return result[1]

def determine_p_q(prices):
    lag_acf = acf(prices, nlags=20)
    lag_pacf = pacf(prices, nlags=20, method='ols')
    q = np.where(lag_acf < 1.96/np.sqrt(len(prices)))[0][0] if np.any(lag_acf < 1.96/np.sqrt(len(prices))) else 0
    p = np.where(lag_pacf < 1.96/np.sqrt(len(prices)))[0][0] if np.any(lag_pacf < 1.96/np.sqrt(len(prices))) else 0
    return p, q

def forecast(symbol, start_date, end_date):
    data = download_historical_data(symbol, start_date, end_date)
    data = data.sort_index()
    prices = data['Close']

    p_value = adf_test(prices)
    d = 0
    while p_value > 0.05:
        d += 1
        prices = prices.diff().dropna()
        p_value = adf_test(prices)

    p, q = determine_p_q(prices)

    model = ARIMA(data['Close'], order=(p, d, q))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=10)
    
    return forecast.to_json()