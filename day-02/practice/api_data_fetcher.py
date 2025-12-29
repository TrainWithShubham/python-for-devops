import requests
import json

# Base URL for the Advice Slip API
BASE_URL = "https://api.adviceslip.com/advice/"

# List to store all collected advice
all_advice = []

# Loop through advice IDs 1 to 10
for slip_id in range(1, 11):
    response = requests.get(f"{BASE_URL}{slip_id}")

    # Convert response to JSON
    data = response.json()

    # Check if advice exists
    if "slip" in data:
        advice_data = {
            "id": data["slip"]["id"],
            "advice": data["slip"]["advice"]
        }

        # Store advice
        all_advice.append(advice_data)

        # Print readable output
        print(f"[{advice_data['id']}] {advice_data['advice']}")
    else:
        print(f"[{slip_id}] No advice found")

# Save collected advice to a JSON file
with open("advice_1_to_10.json", "w", encoding="utf-8") as file:
    json.dump(all_advice, file, indent=4, ensure_ascii=False)

print("\nAdvice saved to advice_1_to_10.json")
