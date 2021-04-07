import flask
from . import app
from . import forms

@app.route("/")
def home():
    return "Hello You!"

@app.route("/about")
def about():
    return flask.render_template("about.html")

@app.route("/sign-up", methods=["GET","POST"])
def signup():
    form = forms.SignUpForm()
    if flask.request.method == "POST":
        print("Name: ", form.username.data)
        print("Password:", form.password.data)

    return flask.render_template("sign-up.html", form=form)
