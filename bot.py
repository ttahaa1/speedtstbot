from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# استبدل التوكن بالرمز الخاص بك
updater = Updater(token='6559175304:AAHfpapBsI9VAwtaja-0LhnlMt-Y5WOWw3U', use_context=True)

def start(update, context):
    welcome_message = "أهلاً بك في بوت التواصل! أرسل رسالتك وسأقوم بالرد عليك فيما بعد."
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)

def forward_message(update, context):
    user_id = update.message.from_user.id
    forwarded_from_user_id = update.message.forward_from.id if update.message.forward_from else None
    if forwarded_from_user_id and user_id != forwarded_from_user_id:
        user_name = update.message.from_user.username
        message = f"{user_name}: {update.message.text}"
        context.bot.forward_message(chat_id='6264668799', from_chat_id=update.message.chat_id, message_id=update.message.message_id)
        reply_text = "تم إرسال رسالتك بنجاح وسأقوم بالرد عليك في أقرب وقت ممكن."
        context.bot.send_message(chat_id=forwarded_from_user_id, text=reply_text)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="عذراً، لا يمكن إعادة إرسال رسالتك.")

start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)

forward_handler = MessageHandler(Filters.text & (~Filters.command), forward_message)
updater.dispatcher.add_handler(forward_handler)

updater.start_polling()
updater.idle()
