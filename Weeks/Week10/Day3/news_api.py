# api_key: 5719809a4f814d0d9f8cb98e7a3d97de
# https://newsapi.org/s/google-news-api
# https://newsapi.org/docs/endpoints/top-headlines
# Make a request on a url: requests.get("theurl.com", params={})
# r = requests.get("theurl.com", params={})
# To get the content of the result:
# r.text
# https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY

# Eyal solution:
# # Dont call your file "json.py"
import json
import requests     # "Module not found" --> pip install requests

url = "https://newsapi.org/v2/everything"
token = "5719809a4f814d0d9f8cb98e7a3d97de"
params = {
    "apiKey": token,
    "q": "Meghan",
    "from": "2021-03-01"
}

results = requests.get(url, params=params)

results_dict = json.loads(results.text) # results.json()

for article in results_dict["articles"][:5]:
    print(article["title"])


# import json
# import requests
# r = requests.get("https://newsapi.org/v2/top-headlines?apiKey=5719809a4f814d0d9f8cb98e7a3d97de", params={"q": "Bitcoin","pagesize": 5})
# string_text = r.text
# print(r.text)
# print(type(r.text))

# dict_text = json.loads(string_text)
# print(dict_text)
# print(type(dict_text))

# for i in range(2):
#     print(dict_text["articles"][i]["title"])

