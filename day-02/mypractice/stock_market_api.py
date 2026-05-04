import requests

API_KEY = "DAZR72VR6C6AVTHW"

API_URL = "https://www.alphavantage.co/"

#symbol = "IBM"

def get_stock_market_data(symbol,is_time_series):

      

    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

    #print(API_URL+query)

    response = requests.get(url=API_URL+query)
    for item,value in response.json().items():
        if is_time_series == "yes":
    
          print(item,value)


        else :
           if  item == "Meta Data":
                  print(item,value)      
        
symbol = input("Enter the stock symbol(IBM,GOGL,AMZN): ")
is_time_series = input("Do you want to see the time series data? (yes/no): ")

            
get_stock_market_data(symbol,is_time_series)
 