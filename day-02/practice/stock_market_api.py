import requests

API_KEY = "QRHE86JT0WVBQLHI" # Step 1 get API key

api_url = "https://www.alphavantage.co/" # Step 2 find a base URL


def get_stock_market_data(symbol,is_timeseries):
    if is_timeseries:
        query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    else:
        query = f"query?symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url=api_url+query)
    for key, value in response.json().items():
        if is_timeseries:
            
            print(key,value)
        else:
            if key == "Time Series (Daily)":
                continue


symbol = input("Enter the Symbol you want for the Stock Market API eg. (AMZN, GOGL, IBM, etc)")
is_timeseries = True
get_stock_market_data(symbol,is_timeseries)