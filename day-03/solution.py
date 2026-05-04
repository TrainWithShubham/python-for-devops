import requests

API_KEY = "DAZR72VR6C6AVTHW"
API_URL = "https://www.alphavantage.co/"

def get_stock_market_data(symbol, is_time_series):
    try:
        query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(url=API_URL + query, timeout=10)
        response.raise_for_status()

    except requests.exceptions.ConnectionError:
        print("❌ No internet connection. Please check your network.")
        return
    except requests.exceptions.Timeout:
        print("❌ Request timed out. The server took too long to respond.")
        return
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error occurred: {e}")
        return

    try:
        data = response.json()

    except requests.exceptions.JSONDecodeError:
        print("❌ Failed to parse response. The API may have returned invalid data.")
        return

    try:
        # ✅ Check FIRST before doing anything else
        if "Error Message" in data:
            print(f"❌ Invalid stock symbol '{symbol}'. Please enter a valid symbol like IBM, GOOGL, AMZN.")
            return

        if "Note" in data:
            print(f"⚠️ API Limit Reached: {data['Note']}")
            return

        if "Meta Data" not in data:
            print("❌ Unexpected response from API. No data found.")
            return

        # ✅ Only reaches here if symbol is valid
        print(f"\n✅ Fetching data for: {symbol}")

        for item, value in data.items():
            if is_time_series == "yes":
                print(f"\n{item}:")
                print(value)
            else:
                if item == "Meta Data":
                    print(f"\n{item}:")
                    print(value)

    except KeyError as e:
        print(f"❌ Unexpected data format. Missing key: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# --- Main Program ---
try:
    symbol = input("Enter the stock symbol (IBM, GOOGL, AMZN): ").strip().upper()
    if not symbol:
        raise ValueError("Stock symbol cannot be empty.")

    is_time_series = input("Do you want to see the time series data? (yes/no): ").strip().lower()
    if is_time_series not in ("yes", "no"):
        raise ValueError("Please enter only 'yes' or 'no'.")

except ValueError as e:
    print(f"❌ Invalid input: {e}")

else:
    get_stock_market_data(symbol, is_time_series)