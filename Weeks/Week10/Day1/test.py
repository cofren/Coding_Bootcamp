import requests

token = "1600362325:AAH4cjoJXbJrk_ZtbVylW5jI3QHAk-5vgis"

method_url = f"https://api.telegram.org/bot{token}"

get_me = method_url + "/getMe"

def get_messages():
    get_updates = method_url + "/getUpdates"

    # r = requests.get(get_me)
    r = requests.get(get_updates)
 
    return r.json()

def send_messages("624392869","test"):
    send_message = method_url + "/sendMessage"
    # user_id = 24392869

msgs = get_messages()
send_messages()
print(msgs['result'])

#get Updates

