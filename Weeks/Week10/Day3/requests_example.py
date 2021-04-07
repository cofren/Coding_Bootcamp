import requests
import json

keyword = input("Please enter a keyword: ")

token = "2e4f47b8daec4d4882e41b85a87faf43"
url = f"https://newsapi.org/v2/everything?apiKey={token}"
params = {
    "q": keyword,
    "from": "2021-03-01",
    "pageSize": 5,
    "language": "de"
}

results = requests.get(url, params)
# print(results.text)
# print(type(results.text))

results_dict = json.loads(results.text)
print(results_dict)
# print(type(results_dict))

only_keys = results_dict.keys()
print(only_keys)

for article in results_dict["articles"]:
    only_title = article["author"]
    print(only_title)
