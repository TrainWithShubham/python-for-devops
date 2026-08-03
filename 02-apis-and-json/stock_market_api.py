# Call an API that needs a key - read the key from the environment, never hardcode it.
# Get a free key at https://www.alphavantage.co/support/#api-key
# then: export ALPHAVANTAGE_API_KEY="your_key_here"

import os
import sys

import requests

BASE_URL = "https://www.alphavantage.co/query"


def get_daily_series(symbol, api_key):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key,
    }
    response = requests.get(BASE_URL, params=params, timeout=15)
    response.raise_for_status()
    return response.json()


def main():
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
    if not api_key:
        print("Set ALPHAVANTAGE_API_KEY first:  export ALPHAVANTAGE_API_KEY=MCHYRHM0ME21PCKH")
        sys.exit(1)

    symbol = input("Enter a stock symbol (e.g. IBM, AMZN, GOOGL): ").strip().upper()
    data = get_daily_series(symbol, api_key)

    series = data.get("Time Series (Daily)")
    if not series:
        # Alpha Vantage returns a "Note" or "Information" message on rate limit.
        print("No time series returned:", data)
        return

    for date in list(series)[:5]:
        close = series[date]["4. close"]
        print(f"{date}  close={close}")


if __name__ == "__main__":
    main()
