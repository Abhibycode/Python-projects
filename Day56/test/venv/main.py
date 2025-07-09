from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("./templates/index.html")

@app.route("/tom")
def tom():
    return "<h2>Tom's home</h2>"

if __name__ == "__main__":
    app.run(debug=True)
