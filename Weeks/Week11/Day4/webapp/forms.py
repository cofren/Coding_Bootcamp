import flask_wtf
import wtforms

class TestForm(flask_wtf.FlaskForm)

    name = wtforms.StringField("Name: ")
    age = wtforms.IntegerField("Age: ")

    submit = wtforms.SubmitField("Submit the form !")
    