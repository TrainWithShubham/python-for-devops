import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1" # server URL (API)

response = requests.get(url=api_url)

for key,value in response.json().items():
    if key == "userId":
        if value in [100,200,300]:
            print("User found")