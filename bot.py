import telebot

BOT_TOKEN = "7522961870:AAHRyyyW8RRBNVsXRXKzlUGaAo6Cp7uq8mk"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبا بك في بوت التوقعات! 🎯")

bot.polling()
