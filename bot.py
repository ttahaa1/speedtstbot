from flask import Flask, request
import requests
from bs4 import BeautifulSoup
import telegram
from telegram.ext import Updater, CommandHandler
import logging

# إعداد تسجيل المعلومات
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
TOKEN = '6743547187:AAGfhT8wv-Z9Ds2NP_xItJs0Ud89o0qvyYE'
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! Send /download followed by the TikTok video URL to get the download link.")

def download(update, context):
    if len(context.args) > 0:
        tiktok_url = context.args[0]
        download_link = get_download_link(tiktok_url)
        if download_link:
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Here is your download link: {download_link}")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Error retrieving download link.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide a TikTok video URL.")

def get_download_link(tiktok_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    data = {
        'id': tiktok_url,
        'locale': 'en',
        'tt': 'Z2V0aW5mby5wb2w=',
    }
    response = requests.post('https://ssstik.io/abc', headers=headers, data=data)
    
    logging.info(f"Status Code: {response.status_code}")
    logging.info(f"Response Text: {response.text}")

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        logging.info(f"Soup Content: {soup.prettify()}")  # طباعة محتوى الصفحة بشكل جميل
        download_link = soup.find('a', {'id': 'download-link'})  # حاول إيجاد الرابط بناءً على معرفه
        if download_link:
            return download_link['href']
        else:
            logging.error("Download link not found in the response.")
    else:
        logging.error(f"Failed to retrieve the page, status code: {response.status_code}")
    return None

start_handler = CommandHandler('start', start)
download_handler = CommandHandler('download', download)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(download_handler)

updater.start_polling()

if __name__ == "__main__":
    app.run(port=8443)
