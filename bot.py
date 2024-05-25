import os

# Check if the library is installed, if not, install it
try:
    import telegram
except ImportError:
    os.system("pip install python-telegram-bot")

# Import necessary modules
from telegram.ext import Updater, MessageHandler, Filters

# Define your bot token and your user ID
TOKEN = '7094426542:AAGXW6_WzTFx9ovc4Ywtv8UPL-GuBiyI2ig'
YOUR_ID = '5691350382'

# Define the function to forward messages
def forward_message(update, context):
    # Check the user ID of the sender
    user_id = update.message.from_user.id
    
    # If the user ID matches your ID, forward the message to yourself
    if str(user_id) == YOUR_ID:
        context.bot.forward_message(chat_id=YOUR_ID, from_chat_id=update.message.chat_id, message_id=update.message.message_id)

# Initialize the bot updater with your bot's token
updater = Updater(token=TOKEN, use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register a message handler to handle incoming messages
forward_handler = MessageHandler(Filters.text & (~Filters.command), forward_message)
dispatcher.add_handler(forward_handler)

# Start the bot
updater.start_polling()
updater.idle()
