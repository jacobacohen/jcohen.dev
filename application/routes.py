from application import app
from flask import render_template

@app.route("/")
@app.route("/home.html")
@app.route("/index.html")
def index():
    return render_template("index.html", index=True)

@app.route("/other.html")
def other():
    return render_template("other.html")
