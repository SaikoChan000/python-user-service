from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello!</p>"

@app.route("/banane")
def banane():
    return "Apfel!"

@app.route("/apfel")
def apfel():
    return "Melone!"

@app.route('/user/<username>/<password>')
def show_user_profile(username, password):
    if password == "12345":
        return username
    return "Wrong password!"