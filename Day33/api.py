import requests

results = requests.get(url="http://api.open-notify.org/iss-now.json")
print(results.content)
data = results.json()
if results.status_code == 200:
    print(f"{results.status_code}: {data["message"]}")
print(results.raise_for_status())

print(data["iss_position"]["longitude"])
print(data["iss_position"]["latitude"])