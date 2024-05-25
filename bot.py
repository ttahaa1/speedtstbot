import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# تمكين تسجيل الأخطاء
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# توكن البوت
BOT_TOKEN = "6743547187:AAGfhT8wv-Z9Ds2NP_xItJs0Ud89o0qvyYE"
# معرف التليجرام الخاص بك
ADMIN_CHAT_ID = "6264668799"

# قائمة لتخزين الرسائل
messages_list = []

# دالة بدء التشغيل
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('مرحباً! كيف يمكنني مساعدتك؟')
    logger.info("Start command received")

# دالة الرد على الرسائل النصية وإشعارك
async def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    user_id = update.message.chat_id
    user_name = update.message.chat.username
    message_date = update.message.date  # استرجاع وقت استقبال الرسالة

    # إضافة الرسالة إلى قائمة الرسائل
    messages_list.append({
        "text": user_message,
        "user_id": user_id,
        "user_name": user_name,
        "message_date": message_date
    })

    # إرسال رسالة إلى المستخدم
    await update.message.reply_text(f"لقد تلقيت رسالتك: {user_message}")
    logger.info(f"Message from {user_name} (ID: {user_id}): {user_message}")

    # إرسال إشعار إلى الأدمن
    try:
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=f"رسالة جديدة من {user_name} (ID: {user_id}) في {message_date}: {user_message}"  # إضافة وقت الرسالة
        )
        logger.info(f"Notification sent to admin: {ADMIN_CHAT_ID}")
    except Exception as e:
        logger.error(f"Failed to send notification: {e}")

# دالة تسجيل الأخطاء
def error(update: object, context: CallbackContext) -> None:
    logger.warning(f'Update "{update}" caused error "{context.error}"')

def main() -> None:
    # إعداد البوت باستخدام التوكن
    application = Application.builder().token(BOT_TOKEN).build()

    # ربط الأوامر والدوال المناسبة
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # تسجيل الأخطاء
    application.add_error_handler(error)

    # بدء تشغيل البوت
    application.run_polling()

if __name__ == '__main__':
    main()
