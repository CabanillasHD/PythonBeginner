import os
import requests
from dotenv import load_dotenv
import telebot

load_dotenv()

BOT_API = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(BOT_API)

@bot.message_handler(commands=['start'])
def initial_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Hello, World!')


bot.polling()