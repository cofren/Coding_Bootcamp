import requests
import json

url = "https://newsapi.org/v2/everything"
token = "2e4f47b8daec4d4882e41b85a87faf43"

def get_news(query):
    params = {
        "apiKey": token,
        "q": query,
        "pageSize": 10
        
    }

    results = requests.get(url, params=params)
    return json.loads(results.text)['articles']
