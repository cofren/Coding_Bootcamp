from . import app
import datetime
import flask
from . import forms

@app.route("/")
def home():
    return "Hello"

@app.route("/About2")
def about():
    return flask.render_template("about.html")

@app.route("/Greeting")
def time():
    d = datetime.datetime.now()
    return flask.render_template("greeting.html", date_obj = d)

@app.route("/Hello")
def hello():
    return flask.render_template("hello.html")

@app.route("/Products")
def products():
    return flask.render_template("products.html")

@app.route('/test-form')
def test():
    form = forms.TestForm()

    return flask.render_template("test_form.html", form=form)