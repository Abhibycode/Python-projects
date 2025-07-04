import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 17.6614522 # Your latitude
MY_LONG = 75.8362153 # Your longitude

def is_iss_overhead():
    value = True
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        pass
    else:
        value = False
    return value


def is_night():
    night = True
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        pass
    else:
        night = False

    return night
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com", port=587) as emails:
            emails.starttls()
            emails.login(user="abhikongari123@gmail.com", password="bluuwifbidjkzpjt")
            emails.sendmail(from_addr="abhikongari123@gmail.com",
                            to_addrs="eternaltimestogo@gmail.com",
                            msg="Subject: Look Up\n\nYou will see satellite and a beautiful sky")