import json
import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

dict_text = json.loads(response.text)
# print(dict_text)

pretty_text = json.dumps(dict_text,indent=2)
print(pretty_text)
