import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.constants import ChatMemberStatus

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_USERNAME = "@tm_ad_gsr"
PDF_FILE = "5_errors_interior_state_detailed.pdf"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Спасибо за подписку! Вот ваш файл:")
            await context.bot.send_document(chat_id=update.effective_chat.id, document=open(PDF_FILE, "rb"))
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id,
                text=f"Чтобы получить PDF, подпишись на канал {CHANNEL_USERNAME} и снова нажми /start.")
    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id,
            text="Не удалось проверить подписку. Убедись, что бот добавлен в админы канала.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
