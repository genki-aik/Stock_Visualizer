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

tickers = ['GOOG', 'MSFT', 'SPY']
df = yf.download(tickers, start='2019-01-01', end='2020-08-30')['Adj Close']

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

#get_close_price('GME', '2020-12-01', '2021-01-30')