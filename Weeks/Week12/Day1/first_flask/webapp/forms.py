import flask_wtf
import wtforms

class SignUpForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Username: ")
    password = wtforms.PasswordField("Password: ")
    
    submit = wtforms.SubmitField("Sign me up!")