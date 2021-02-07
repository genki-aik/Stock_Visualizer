import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

#df = yf.download("MSFT", start='2019-01-01', end='2020-05-30')['Adj Close']

# def get_adjusted_close(ticker, beginning, ending):
#     return yf.download(ticker, start=beginning, end=ending)['Adj Close']

# Create the close graph for one stock
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

# Create graph for cumulative returns
# Needs at least 2 tickers to compare and visualize
def cumulative_return(beginning, ending, *tickers):

    #tickers = ['GOOG', 'MSFT', 'SPY']
    tickers = list(tickers)
    
    if (len(tickers) < 2):
        raise ValueError("More than 2 tickers are needed to compare cumulative returns!")
       

    df = yf.download(tickers, start=beginning, end=ending)['Adj Close']

    plt.style.use('seaborn')

    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot cumulative returns for each symbol
    for ticker in tickers:
        ax.plot((df[ticker].pct_change()+1).cumprod()-1, label=ticker)

    ax.legend()

    # Show y axis in %
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

    title = 'Cumulative Returns - ' + ', '.join(s for s in tickers)
    plt.title(title, fontsize=16)

    # Define the labels for x-axis and y-axis
    plt.ylabel('Cumulative Returns %', fontsize=14)
    plt.xlabel('Year', fontsize=14)

    plt.show()
    plt.close()

# Moving average graph
def moving_average(ticker, beginning, ending):
    stock = yf.download(ticker, beginning, ending)['Adj Close']
    

    plt.style.use('seaborn')
    fig, ax = plt.subplots(figsize=(12, 6))

    # Calculate 20 and 100 days moving averages of closing prices
    stock_20_ma = stock.rolling(window=20).mean()
    stock_100_ma = stock.rolling(window=100).mean()

    # Start from 2019-05-24 as there are no data before for 100-day
    start_date = '2019-05-24 00:00:00'
    ax.plot(stock[start_date:], label='MSFT')
    ax.plot(stock_20_ma[start_date:], label='20 days MA')
    ax.plot(stock_100_ma[start_date:], label='100 days MA')

    ax.legend()

    plt.title('Adjusted Close Price - ' + ticker, fontsize=16)

    # Define labels for x and y axis
    plt.ylabel('Adjusted Close Price ($)', fontsize=14)
    plt.xlabel('Year', fontsize=14)

    plt.show()
    plt.close()

#get_close_price('GME', '2020-12-01', '2021-01-30')
cumulative_return('2019-01-01', '2020-12-30', 'AAPL')
#moving_average('MSFT', '2019-05-24', '2020-12-30')
