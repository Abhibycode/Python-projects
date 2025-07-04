from os.path import split

import requests
import datetime

parameters = {
    "lat": 17.6614522,
    "lng": 75.8362153,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset)
print(sunrise)

now = datetime.datetime.now()
now.astimezone()
print(now.hour)