import dotenv
import telebot
import os
from utils import get_battle_royale_current_map, get_map_informations, get_server_status

dotenv.load_dotenv()
API_KEY_TELEGRAM = os.environ.get('API_KEY_TELEGRAM')
bot = telebot.TeleBot(API_KEY_TELEGRAM)

@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, """
        Hi there 👋🏼, I am Apex Update Notifier Bot. I notify you with some useful informations about Apex Legends!
        """)

@bot.message_handler(commands=['map'])
def map(message):
    bot.send_message(message.chat.id, get_map_informations(get_battle_royale_current_map()))

"""
@bot.message_handler(commands=['status'])
def status(message):
    bot.send_message(message.chat.id, get_server_status())
"""
bot.infinity_polling()