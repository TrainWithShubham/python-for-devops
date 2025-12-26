import requests
import json

API_KEY = "1e270302a65f266e09593ed9a5c39fa4" # Step 1 get API key

BASE_URL = "https://api.ipstack.com/" # Step 2 find a base URL

def fetch_ip_data(ip_address):
    url = f"{BASE_URL}{ip_address}?access_key={API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def process_ip_data(data):
    processed_data = {
        "IP": data.get("ip"),
        "Type": data.get("type"),
        "Continent": data.get("continent_name"),
        "Country": data.get("country_name"),
        "Region": data.get("region_name"),
        "City": data.get("city"),
        "Latitude": data.get("latitude"),
        "Longitude": data.get("longitude"),
        "ISP": data.get("connection", {}).get("isp"),
    }
    return processed_data


def save_to_json(data, filename="output.json"):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def main():
    ip_address = input("Enter an IP address: ")
    raw_data = fetch_ip_data(ip_address)
    processed_data = process_ip_data(raw_data)

    print("Processed IP Data:")
    for key, value in processed_data.items():
        print(f"{key}: {value}")

    save_to_json(processed_data)
    print(f"Data saved to output.json")


if __name__ == "__main__":
    main()