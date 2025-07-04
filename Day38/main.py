import requests
import datetime

APPLICATION_ID = "7b49d468"
API_KEY = "6410d97ca592b9c5537932c7054f38cf"
SHETTY_TOKEN = "https://api.sheety.co/"
SHETTY_URL = "/f16b2ea0018a0e2b934c6f6e26664156/caloriesCounter/sheet1"
SHETTY_AUTH = "a2FiaGkxOTk4OkVhcnRoIzYxNg=="

nutrion_endpoint = "https://trackapi.nutritionix.com/v2"
shetty_endpoint = "https://api.sheety.co"


TODAY = datetime.datetime.now()

def get_calories(text):
    exercises_url = f"{nutrion_endpoint}/natural/exercise"
    body = {
        "query": text,
        "gender": "male",
        "weight_kg": 107,
        "height_cm": 169,
        "age": 26
    }
    header = {
        'x-app-id': APPLICATION_ID,
        'x-app-key': API_KEY,
        "x-remote-user-id": "0"
    }

    response = requests.post(url=exercises_url, json=body, headers=header)
    response.raise_for_status()
    print(response.text)
    return response.json()["exercises"]

def add_entry(entry):
    shetty_url = shetty_endpoint + SHETTY_URL
    body = {
        "sheet1": {
            "Date" : TODAY.strftime("%Y-%m-%d"),
            "Time": TODAY.strftime("%H:%M"),
            "Exercise": entry["user_input"].title(),
            "Duration": f"{entry["duration_min"]} min",
            "Calories": f"{entry['nf_calories']} kcal"
        }
    }
    header = {
        "Authorization": f"Basic {SHETTY_AUTH}"
    }

    response = requests.post(url=shetty_url, json=body, headers=header)
    response.raise_for_status()
    print(response.content)

print("What exercise you did today?")

while True:
    activity = input(">")
    if activity == "":
        print("Please enter an exercise")
    else:
        break

exercise_list = get_calories(activity)

for exercise in exercise_list:
    add_entry(exercise)