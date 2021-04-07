import flask
from . import app
from . import forms,news_function

@app.route("/")
def home():
    return "HelloYou!"

@app.route("/signup")
def sign():
    form = forms.Signup()

    return flask.render_template("signup.html", form=form)


@app.route("/search", methods=["POST","GET"])
def search():
    form = forms.QueryForm()

    if flask.request.method == "POST":
        return flask.redirect(flask.url_for("articles", query=form.query.data))

    return flask.render_template("search.html",form=form)

@app.route("/articles/<query>")
def articles(query):
    articles = news_function.get_news(query)
    return flask.render_template("articles.html", articles=articles)
















# @app.route("/search", methods=["POST","GET"])
# def search():
#     form = forms.QueryForm()

#     if flask.request.method == "POST":
#         return flask.redirect(flask.url_for("articles", query=form.query.data))
    
#     return flask.render_template("search.html",form=form)


# @app.route("/articles/<query>")
# def articles(query):
#     articles = news_function.get_news(query)
#     return flask.render_template("articles.html", articles=articles)









# @app.route("/search", methods=["GET","POST"])
# def search():
#     form = forms.QueryForm()

#     if flask.request.method == "POST":
#         return flask.redirect(flask.url_for("articles", query=form.query.data))

#     return flask.render_template("search.html", form=form)

# @app.route("/articles/<query>")
# def articles(query):
#     articles = news_function.get_news(query)
#     return flask.render_template("articles.html", articles=articles)








# @app.route("/search_article", methods=["GET","POST"])
# def search_article():
#     form = forms.QueryForm()

#     if flask.request.method == "POST":
#        return flask.redirect(flask.url_for("query_article",query=form.query.data))
    
#     return flask.render_template("/search_article.html",form=form)

# @app.route("/article/query/<query>")
# def query_article(query):
#     articles = news_function.get_news(query)
#     return flask.render_template("articles.html", articles=articles)

