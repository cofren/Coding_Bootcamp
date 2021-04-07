import flask

app = flask.Flask(__name__)

# In case you a "A scret key "
app.config["SECRET_KEY"] = "my-very-secret-key"

from . import routes