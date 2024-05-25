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
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
# معرف التليجرام الخاص بك
ADMIN_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

# دالة بدء التشغيل
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('مرحباً! كيف يمكنني مساعدتك؟')

# دالة الرد على الرسائل النصية وإشعارك
async def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    user_id = update.message.chat_id
    user_name = update.message.chat.username

    # إرسال رسالة إلى المستخدم
    await update.message.reply_text(f"لقد تلقيت رسالتك: {user_message}")

    # إرسال إشعار إلى الأدمن
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"رسالة جديدة من {user_name} (ID: {user_id}): {user_message}"
    )

def main() -> None:
    # إعداد البوت باستخدام التوكن
    application = Application.builder().token(BOT_TOKEN).build()

    # ربط الأوامر والدوال المناسبة
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # تسجيل الأخطاء
    application.add_error_handler(lambda update, context: logger.warning(f'Update "{update}" caused error "{context.error}"'))

    # بدء تشغيل البوت
    application.run_polling()

if __name__ == '__main__':
    main()
