import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

df = yf.download("MSFT", start='2019-01-01', end='2020-05-30')['Adj Close']

def get_adjusted_close(ticker, beginning, ending):
    return yf.download(ticker, start=beginning, end=ending)['Adj Close']


def get_close_price(ticker, beginning, ending):
    # Register the converters
    pd.plotting.register_matplotlib_converters()

    # Load Data
    #df = yf.download("MSFT", start='2019-01-01', end='2020-05-30')['Adj Close']
    df = yf.download(ticker, start = beginning, end = ending)['Adj Close']

    # Set style to seaborn
    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot the cumulative returns for each symbol
    ax.plot(df)
    ax.legend()

    plt.title('Adjusted Close Price - MSFT', fontsize=16)

    # Define the labels for x-axis and y-axis
    plt.ylabel('Adjusted Close Price', fontsize=14)

    plt.xlabel('Year', fontsize=14)
    plt.show()
    plt.close()

get_close_price('GME', '2020-12-01', '2021-01-30')