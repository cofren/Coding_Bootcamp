import flask
from . import app
from . import forms

@app.route("/")
def home():
    return flask.render_template("home.html")

@app.route("/sign")
def sign():
    form = forms.Signme()

    return flask.render_template("signme.html", form=form)

