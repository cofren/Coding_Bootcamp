#!/usr/bin/python3

##############################################
#
# first.py
# 14_03_flask1
#
##############################################
import flask
import random
import datetime

import requests     # "Module not found" --> pip install requests

url = "https://newsapi.org/v2/everything"
token = "5719809a4f814d0d9f8cb98e7a3d97de"

def get_news(query):
    params = {
        "apiKey": token,
        "q": "query",
        "from": "2021-03-01"
    }

    results = requests.get(url, params=params)
    return results.json()['articles']

# Create a controller using flask.Flask class
app = flask.Flask(__name__)     # __name__ is the name of the file

# Create one route: a function that is assigned to a URL
# 127.0.0.1:5000/ <--> route "/"
# 127.0.0.1:5000/home <--> route "/home"
@app.route("/")
@app.route("/home") # --> Will assign the function to www.yourdomain.com/home
def homepage():
    return "<html><body><h3> Hello world ! </h3></body></html>"

# He sees a random number between 1 and 100 on his screen
@app.route("/random-number")
def random_number():
    number = random.randint(1, 100)
    return f"Your number is: {number}"

# 127.0.0.1:5000/greet/eyal --> Hello, eyal, nice to see you
# 127.0.0.1:5000/greet/rick

@app.route("/greet/<name>")
def greeting_message(name):
    # Render the greet.html template passing name as name
    return flask.render_template("greet.html", name=name)

@app.route('/news/<topic>')
def news(topic):
    articles = get_news(topic)[:5]

    return flask.render_template("articles.html", articles=articles)

@app.route("/hour")
def hour():
    """
    Page that displays the hour, if the hour is later than 20:00, display a good night message
    """
    d = datetime.datetime.now()
    return flask.render_template("hour.html", date_obj=d)


# Run the application server
app.run(port=5001, debug=True)


