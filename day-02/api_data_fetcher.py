import requests
import json


api_url = "https://official-joke-api.appspot.com/random_joke"

def get_jokes():
    response = requests.get(url=api_url)
    print(response.json())
    # final = json.loads(response.text) 
    # print(final)
    # new_final = json.dumps(final)
    with open ("jokes.json" , "w") as json_file:
       json_file.write(response.text)
       print("data written to json file successfully")
    for key,value in response.json().items():
     setup = response.json()["setup"]
     punchline = response.json()["punchline"]
     return setup, punchline
setup, punchline = get_jokes()
print(setup)
print(punchline)