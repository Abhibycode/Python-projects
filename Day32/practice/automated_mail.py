import random
import smtplib
import datetime

now = datetime.datetime.now()
weekday = now.weekday()

MY_EMAIL = "abhikongari123@gmail.com"
MY_PASSWORD = "bluuwifbidjkzpjt"

if weekday == 1:
    with open("quotes.txt", mode="r") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)
    print(quote)
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connections:
        connections.starttls()
        connections.login(user="abhikongari123@gmail.com", password=MY_PASSWORD)
        connections.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Monday Blues\n\n{quote}")
        connections.close()
