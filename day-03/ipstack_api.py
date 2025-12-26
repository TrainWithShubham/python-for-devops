import requests
import json


API_KEY = "1e270302a65f266e09593ed9a5c39fa4"
BASE_URL = "http://api.ipstack.com/"


def fetch_ip_data(ip_address):
    try:
        url = f"{BASE_URL}{ip_address}?access_key={API_KEY}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"[ERROR] Failed to fetch API data: {error}")
        return None


def process_ip_data(api_response):
    if not api_response or "error" in api_response:
        print("[ERROR] Invalid API response received")
        return None

    return {
        "ip": api_response.get("ip"),
        "country": api_response.get("country_name"),
        "region": api_response.get("region_name"),
        "city": api_response.get("city"),
        "latitude": api_response.get("latitude"),
        "longitude": api_response.get("longitude"),
        "isp": api_response.get("connection", {}).get("isp"),
    }


def save_to_json(data, filename="output2.json"):
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as error:
        print(f"[ERROR] Failed to write file: {error}")


def main():
    ip_address = input("Enter an IP address (example: 8.8.8.8): ").strip()

    if not ip_address:
        print("[ERROR] IP address cannot be empty")
        return

    api_response = fetch_ip_data(ip_address)
    processed_data = process_ip_data(api_response)

    if not processed_data:
        print("[INFO] No data to display")
        return

    print("\nIP Information:\n")
    for key, value in processed_data.items():
        print(f"{key}: {value}")

    save_to_json(processed_data)
    print("\nData saved successfully to output2.json")


if __name__ == "__main__":
    main()
