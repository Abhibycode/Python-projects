##################### Extra Hard Starting Project ######################
import random
import smtplib
import pandas
import datetime


MY_EMAIL = "abhikongari123@gmail.com"
MY_PASSWORD = "bluuwifbidjkzpjt"

now = datetime.datetime.now()
now_details = (now.month, now.day)

# 1. Update the birthdays.csv
data = pandas.read_csv(fr"birthdays.csv")
DOB_details = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if now_details in DOB_details:
    birthday_person = DOB_details[now_details]
    print(birthday_person)
    filepath = fr"C:\Users\Abhishek\Desktop\100 days of python\Day32\birthday_wisher\letter_templates\letter_{random.randint(1, 3)}.txt"
    with open(filepath) as letters:
        contents = letters.read()
        letter = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as mail:
        mail.starttls()
        mail.login(MY_EMAIL, MY_PASSWORD)
        mail.sendmail(from_addr=MY_EMAIL,
                      to_addrs=birthday_person["email"],
                      msg=f"Subject: Happy Birthday\n\n{letter}")