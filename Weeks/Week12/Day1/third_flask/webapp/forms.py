import flask_wtf
import wtforms

class Signup(flask_wtf.FlaskForm):
    username = wtforms.StringField("Name: ")
    
    submit = wtforms.SubmitField("Hit me")





class QueryForm(flask_wtf.FlaskForm):
    query = wtforms.StringField("Query Yo: ")

    submit = wtforms.SubmitField("Hit the Jack!")














# class QueryForm(flask_wtf.FlaskForm):
#     query = wtforms.StringField("Query: ")

#     submit = wtforms.SubmitField("Boing!")









# class QueryForm(flask_wtf.FlaskForm):
#     query = wtforms.StringField("Query: ")

#     submit = wtforms.SubmitField("Hit Me!")








# class QueryForm(flask_wtf.FlaskForm):
#     query = wtforms.StringField("Query: ")

#     submit = wtforms.SubmitField("Submit!")