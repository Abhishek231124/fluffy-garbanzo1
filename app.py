from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/hello")
def hello():
    return "Hello"

@app.route("/name")
def name():
    return "Abhishek"

@app.route("/age")
def age():
    return "29"