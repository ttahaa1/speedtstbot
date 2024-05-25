from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

def start(update, context):
    welcome_message = "أهلاً بك في بوت التواصل! أرسل رسالتك وسأقوم بالرد عليك فيما بعد."
    context.bot.send_message(chat_id=update.message.chat_id, text=welcome_message)

def forward_message(update, context):
    user_name = update.message.from_user.username
    message = f"{user_name}: {update.message.text}"
    context.bot.forward_message(chat_id=6264668799, from_chat_id=update.message.chat_id, message_id=update.message.message_id)
    reply_text = "تم إرسال رسالتك بنجاح وسأقوم بالرد عليك في أقرب وقت ممكن."
    context.bot.send_message(chat_id=update.message.chat_id, text=reply_text)

start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)

forward_handler = MessageHandler(Filters.text & (~Filters.command), forward_message)
updater.dispatcher.add_handler(forward_handler)

updater.start_polling()
updater.idle()
