import smtplib

my_email = "abhikongari123@gmail.com"
password = "bluuwifbidjkzpjt"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="abhishekongari@gmail.com", msg="Subject: Let's try\n\n This is body of email where you read all the important part")
    connection.close()