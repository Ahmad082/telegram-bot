from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8741463054:AAHSuPjcIjqaJJ6vyG2RlnjZpPtFhb8CfFc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبًا! البوت يعمل بنجاح 🎉")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("البوت يعمل...")
app.run_polling()