from flask import Flask
from flask import render_template

app = Flask("__main__")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)