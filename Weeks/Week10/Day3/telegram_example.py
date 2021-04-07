import requests
import json
from datetime import datetime

telegram_token = "1600362325:AAH4cjoJXbJrk_ZtbVylW5jI3QHAk-5vgis"
telegram_method_send = "sendMessage"
telegram_method_get = "getUpdates"
telegram_url_send = f"https://api.telegram.org/bot{telegram_token}/{telegram_method_send}"
telegram_url_get = f"https://api.telegram.org/bot{telegram_token}/{telegram_method_get}"
telegram_param_send = {
    "chat_id": "1170803691",
    "text": datetime.today()
}
# telegram_param_get = {
#     "offset": offset+1,
# }


def send_message():
    result_send = requests.post(telegram_url_send,telegram_param_send)
    # requests.get(telegram_url,telegram_param)
    return result_send

send_message()


def get_message(offset):
    result_get = requests.get(telegram_url_get,{"offset": offset+1,})
    return result_get

print(get_message(1))







# {
# "ok":true,
# "result":{"message_id":48,
#         "from":{"id":1600362325,
#         "is_bot":true,
#         "first_name":"Dudu",
#         "username":
#         "dudu_mybot"
#         },
# "chat":{"id":1170803691,"first_name":"A","last_name":"G","username":"lookslikemyname","type":"private"},
# "date":1615377189,
# "text":"Whats up?"}}