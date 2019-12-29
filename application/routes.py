from application import app
from flask import render_template, request

@app.route("/home.html", methods=['GET'])
@app.route("/index.html", methods=['GET'])
@app.route("/", methods=['GET'])
def index():
    platform = request.user_agent.platform
    mobile = ["android", "blackberry", "iphone"]
    if (platform in mobile):
        return render_template("index.html", mobile=True, index=True)
    else:
        return render_template("index.html", mobile=False, index=True)
        

@app.route("/other.html")
def other():
    return render_template("other.html")
