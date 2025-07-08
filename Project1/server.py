import datetime
import random

import requests
from flask import Flask, render_template

app = Flask("__main__")

@app.route("/")
def home():
    random_number = random.randint(1, 9)
    year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year = year)

@app.route("/guess/<name>")
def let_guess(name):
    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    age_response = requests.get(f"https://api.agify.io/?name={name}")
    return render_template("responses.html",name=name, gender=gender_response.json()["gender"], age=age_response.json()["age"])

@app.route("/blog")
def get_blog():
    blog_url = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    return render_template("blog.html", blogs= blog_url.json())

if __name__ == "__main__":
    app.run(debug=True)