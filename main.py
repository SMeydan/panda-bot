from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random
import os
from datetime import time
from datetime import timedelta

TOKEN = "your-token"
CHAT_ID = 123123

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"[LOG] chat_id = {update.effective_chat.id}")
    await update.message.reply_text("Hello! I'm alive 🎉")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

async def randompic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    folder_path = 'pandas'
    files = os.listdir(folder_path)
    random_file = random.choice(files)
    file_path = os.path.join(folder_path, random_file)
    print(f"[LOG] Sending file: {file_path}") 
    with open(file_path, 'rb') as file:
        await update.message.reply_photo(photo=file)

async def send_daily_panda(context: ContextTypes.DEFAULT_TYPE):
    folder_path = 'pandas'
    files = os.listdir(folder_path)
    random_file = random.choice(files)
    file_path = os.path.join(folder_path, random_file)
    print(f"[LOG] Sending daily panda: {file_path}")
    with open(file_path, 'rb') as file:
        await context.bot.send_photo(chat_id=CHAT_ID, photo=file)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("panda", randompic))
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.job_queue.run_repeating(send_daily_panda, interval=timedelta(minutes=30), first=5)
    app.job_queue.run_daily(send_daily_panda, time(hour=12, minute=00, second=25))
    app.run_polling()
