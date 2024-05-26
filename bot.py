import requests
import json
import os

API_KEY = "6743547187:AAGfhT8wv-Z9Ds2NP_xItJs0Ud89o0qvyYE"
admin = "6264668799"

def bot(method, datas=None):
    url = f"https://api.telegram.org/bot{API_KEY}/{method}"
    if datas:
        response = requests.post(url, json=datas)
    else:
        response = requests.get(url)
    content = response.content.decode("utf-8")
    return json.loads(content)

def handle_updates(update):
    message = update.get("message")
    callback_query = update.get("callback_query")
    
    if message:
        handle_message(message)
    elif callback_query:
        handle_callback_query(callback_query)

def handle_message(message):
    # Handle incoming messages
    text = message.get("text")
    chat_id = message["chat"]["id"]
    from_id = message["from"]["id"]
    username = message["from"].get("username")
    first_name = message["from"].get("first_name")
    
    # Your logic for handling messages

def handle_callback_query(callback_query):
    # Handle callback queries
    data = callback_query["data"]
    chat_id = callback_query["message"]["chat"]["id"]
    message_id = callback_query["message"]["message_id"]
    from_id = callback_query["from"]["id"]
    first_name = callback_query["from"]["first_name"]
    
    # Your logic for handling callback queries

def main():
    # Main function to handle updates
    webhook_data = json.loads(requests.get("https://api.telegram.org/bot{}/getWebhookInfo".format(API_KEY)).content.decode("utf-8"))
    update = json.loads(requests.get(f"https://api.telegram.org/bot{API_KEY}/getMe").content.decode("utf-8"))
    username = update["result"]["username"]
    user = update["result"]["first_name"]
    user_id = update["result"]["id"]
    
    # Your logic for handling updates

    # Example: Listening for updates
    update_data = json.loads(requests.get("php://input").content.decode("utf-8"))
    if update_data:
        handle_updates(update_data)

if __name__ == "__main__":
    main()
