from telegram.ext import Updater, MessageHandler, Filters

updater = Updater(token='6743547187:AAGfhT8wv-Z9Ds2NP_xItJs0Ud89o0qvyYE', use_context=True)

def forward_message(update, context):
    # إعادة توجيه الرسالة المستلمة إلى شات معين
    context.bot.forward_message(chat_id='6264668799', from_chat_id=update.message.chat_id, message_id=update.message.message_id)
    # إرسال رسالة تأكيد للمستخدم
    reply_text = "تم إرسال رسالتك بنجاح وسأقوم بالرد عليك في أقرب وقت ممكن."
    context.bot.send_message(chat_id=update.message.chat_id, text=reply_text)

# إعداد MessageHandler لإعادة توجيه الرسائل النصية
forward_handler = MessageHandler(Filters.text & (~Filters.command), forward_message)
updater.dispatcher.add_handler(forward_handler)

# بدء البوت
updater.start_polling()
updater.idle()
