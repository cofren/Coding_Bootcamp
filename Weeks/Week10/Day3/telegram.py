import requests
import time

telegram_token = "1600362325:AAH4cjoJXbJrk_ZtbVylW5jI3QHAk-5vgis"
google_news_token = "2e4f47b8daec4d4882e41b85a87faf43"

current_id = 0

def get_messages(offset):
    get_updates = f"https://api.telegram.org/bot{telegram_token}/getUpdates"
    r = requests.get(get_updates, params={"offset": offset+1}) # Making a request

    return r.json() # Converts the response to a dictionary

def send_message(destination, text):
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    r = requests.get(url, params={"chat_id":destination, "text":text})

    return r

def get_article_about(topic):
    url = f"http://newsapi.org/v2/everything"
    r = requests.get(url, params={"q":topic, "apiKey":google_news_token})

    results = r.json()
    return results["articles"][0]

offset = 0

while True:
    #Listening for a new message
    result = get_messages(offset)
    updates = result["result"]

    if not updates:
        time.sleep(2)
        continue # Going back to the beginning of the loop

    # There is an update !
    for update in updates:

        # Extracting information out of the update
        offset = update["update_id"]
        content = update["message"]["text"]
        sender_id = update["message"]["from"]

        print(f"[*] Received message from {sender_id}: {content}")

        # Retrieving an article about the topic
        article = get_article_about(content)
        pretty_article = f"{article['title']}"

        # Sending it to the user
        send_message(sender_id, pretty_article)
        print(f"[*] Sent a message to {sender_id}: {pretty_article}")


