import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


# Step 1: Fetching Data
def fetch_data(ticker):
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, start='2015-01-01', end='2023-01-01')
    return data['Close']


# Step 2: Calculate Moving Average
def calculate_moving_average(data, window_size):
    return data.rolling(window=window_size).mean()


# Step 3: Main Function
def main():
    ticker = 'TSLA'  # We are focusing on Tesla stock
    data = fetch_data(ticker)

    # Step 4: Calculate moving averages
    short_window = 20  # Short moving average (20 days)
    long_window = 50  # Long moving average (50 days)

    short_moving_avg = calculate_moving_average(data, short_window)
    long_moving_avg = calculate_moving_average(data, long_window)

    # Step 5: Plot the data
    plt.figure(figsize=(14, 7))
    plt.plot(data, label='TSLA Stock Price', color='blue')
    plt.plot(short_moving_avg, label=f'Short Moving Average ({short_window} days)', color='orange')
    plt.plot(long_moving_avg, label=f'Long Moving Average ({long_window} days)', color='green')

    plt.title('TSLA Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.legend()
    plt.grid()
    plt.show()

    print("Done! Check out the graph for TSLA stock price and moving averages.")


if __name__ == "__main__":
    main()







