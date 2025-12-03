import telebot
import requests

BOT_TOKEN = "8599551146:AAGzjGYHJLxb8oCCl0_3_JYeA-UYKoykJfg"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
                 "Send me any file, and I will give you a direct download link! 😎")

@bot.message_handler(content_types=['document', 'video', 'audio', 'photo'])
def file_handler(message):
    try:
        if message.document:
            file_id = message.document.file_id
            file_name = message.document.file_name
        elif message.video:
            file_id = message.video.file_id
            file_name = "video.mp4"
        elif message.audio:
            file_id = message.audio.file_id
            file_name = "audio.mp3"
        elif message.photo:
            file_id = message.photo[-1].file_id
            file_name = "image.jpg"
        else:
            bot.reply_to(message, "Unsupported file type!")
            return

        file_info = bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}"

        bot.reply_to(message, 
                     f"✔️ Your File is Ready!\n\n"
                     f"📄 File Name: {file_name}\n"
                     f"🔗 Direct Download Link:\n{file_url}\n\n"
                     "⛔ Link will work as long as the file exists on Telegram.")

    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")

bot.polling()
