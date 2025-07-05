from flask import Flask

app = Flask(__name__)

app.route("/username/<name>")
def greeting(name):
    return f"Hello, how you are doing {name}"

if __name__ == "__main__":
    app.run(debug=True)

