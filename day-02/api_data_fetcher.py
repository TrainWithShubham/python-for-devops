import requests

key = "017b9f4078ad85cb37bd38e217665943"

base_url = f"https://api.aviationstack.com/v1/airlines?access_key={key}&limit=100"

def get_airline_status():

    response = requests.get(url=base_url)
    airline_list = response.json()["data"]

    for i in range(0,21):
        print(airline_list[i]["airline_name"], end=" ")
        print(airline_list[i]["status"])

get_airline_status()