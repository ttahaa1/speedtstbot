import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# تمكين تسجيل الأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# توكن البوت
BOT_TOKEN = "6743547187:AAGfhT8wv-Z9Ds2NP_xItJs0Ud89o0qvyYE"
# معرف التليجرام الخاص بك
ADMIN_CHAT_ID = "@KOK0KK"

# دالة بدء التشغيل
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحباً! كيف يمكنني مساعدتك؟')

# دالة الرد على الرسائل النصية وإشعارك
def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    user_id = update.message.chat_id
    user_name = update.message.chat.username

    # إرسال رسالة إلى المستخدم
    update.message.reply_text(f"لقد تلقيت رسالتك: {user_message}")

    # إرسال إشعار إلى الأدمن
    context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"رسالة جديدة من {user_name} (ID: {user_id}): {user_message}"
    )

def error(update: Update, context: CallbackContext) -> None:
    """سجل الأخطاء التي تواجهها الدالة."""
    logger.warning(f'Update "{update}" caused error "{context.error}"')

def main() -> None:
    # إعداد البوت باستخدام التوكن
    updater = Updater(BOT_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    # ربط الأوامر والدوال المناسبة
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # تسجيل الأخطاء
    dispatcher.add_error_handler(error)

    # بدء تشغيل البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
