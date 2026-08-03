import json
import requests

username = input("Enter a GitHub username: ")
url = f"https://api.github.com/users/{username}"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.HTTPError:
    print(f"Could not find a GitHub user called '{username}'.")
    exit()

data = response.json()

print("Name        :", data.get("name"))
print("Public repos:", data.get("public_repos"))
print("Followers   :", data.get("followers"))
print("Location    :", data.get("location"))

with open("github_user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("\nSaved full response to github_user.json")