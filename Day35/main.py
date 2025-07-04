import requests

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "988b8b03d3c6022b76cd0bcde5947404"

weather_process = {
    "lat" : 17.68397995193063,
    "lng" : 75.93293149899607,
    "appid": API_KEY
}

response = requests.get(OWN_ENDPOINT, params=weather_process)
response.raise_for_status()
weather_data = response.json()

print(weather_data["list"][0]["weather"][0][id])

will_rain = False
for hour_data in weather_data:
    condition_code = hour_data['weather'][0][id]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring Umbrella")