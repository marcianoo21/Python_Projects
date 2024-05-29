from flask import Flask, render_template
import random
import time
import requests


app = Flask(__name__)

@app.route("/")
def hello():
    current_year = time.strftime("%Y")
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=current_year)

@app.route("/guess/<name>")
def name(name):
    API1 = f"https://api.agify.io?name={name}"
    API2 = f"https://api.genderize.io?name={name}"

    response1 = requests.get(url=API1)
    response2 = requests.get(url=API2)
    
    data1 = response1.json()
    data2 = response2.json()

    age = data1['age']
    gender = data2['gender']

    return render_template('guess.html', name=name, gender=gender, age=age)
        

@app.route("/blog/<num>")
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)