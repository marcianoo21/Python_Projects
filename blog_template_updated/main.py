from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
#TODO wyłuskac id, title, subtitle, body
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/index.html")
def get_all_posts():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)