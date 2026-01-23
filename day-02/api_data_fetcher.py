import requests
import json

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_Pokemon(pokemon_name):
    url = BASE_URL + pokemon_name.lower()
    headers = {
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        print("API is working... \n")

        selected_data = {
            "name": data["name"],
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
          }
        print(json.dumps(selected_data, indent=4))

        with open("output.json", "w", encoding="utf-8") as f:
            json.dump(selected_data, f, indent=4)

        print("Saving data to output.json ")

        return selected_data

    except requests.exceptions.RequestException as e:
        print("API request failed ❌")
        print("Error:", e)

    
    except requests.exceptions.HTTPError:
        print(f"❌ Pokémon '{pokemon_name}' not found!")

    except ValueError:
        print("Invalid JSON response ❌")


# pokemon_data = get_Pokemon()
def main():
    pokemon_name = input("Enter Pokemon Name...Eg.Pikachu,ditto").strip()
    # print("Eg.Pikachu,ditto")

    if not pokemon_name:
        print("Pokemon cannot be empty")

    get_Pokemon(pokemon_name)    

main()