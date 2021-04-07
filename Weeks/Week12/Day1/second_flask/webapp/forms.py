import flask_wtf
import wtforms

class Signme(flask_wtf.FlaskForm):
    username = wtforms.StringField("Username: ")
    submit = wtforms.SubmitField("Hit me!")
