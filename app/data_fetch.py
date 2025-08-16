import yfinance as yf
import pandas as pd
import subprocess

def get_stock_data(symbol, period="5d", interval="1h"):
    """
    Fetch stock data from Yahoo Finance and flatten columns.
    """
    stock = yf.download(symbol, period=period, interval=interval)

    # Reset index to get Date column
    stock = stock.reset_index()

    # Flatten MultiIndex columns (like ('Close','TSLA')) → 'Close'
    if isinstance(stock.columns, pd.MultiIndex):
        stock.columns = [col[0] for col in stock.columns]

    return stock


def get_tweets(query, limit=50):
    """
    Fetch tweets using snscrape (via subprocess).
    If snscrape fails, return an empty DataFrame.
    """
    try:
        command = f"snscrape --max-results {limit} twitter-search '{query}'"
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, encoding="utf-8"
        )
        tweets = [line for line in result.stdout.split("\n") if line.strip()]
        return pd.DataFrame(tweets, columns=["Tweet"])
    except Exception as e:
        return pd.DataFrame([f"Error fetching tweets: {e}"], columns=["Tweet"])
