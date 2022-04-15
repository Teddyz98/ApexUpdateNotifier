import dotenv
import telebot
import os
from utils import get_battle_royale_current_map, get_map_informations, get_server_status_raw, show_region_status

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
    bot.send_message(message.chat.id, get_map_informations(get_battle_royale_current_map()), parse_mode='MarkdownV2')

regions = ["EU-West", "EU-East","US-West","US-East", "Southamerica", "Asia"]
platforms = ["Origin_login","Playstation-Network","Xbox-Live"]

@bot.message_handler(commands=['status'])
def server_status(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        telebot.types.InlineKeyboardButton("EU-West", callback_data="EU-West"),
        telebot.types.InlineKeyboardButton("EU-East", callback_data="EU-East"),
        telebot.types.InlineKeyboardButton("US-West", callback_data="US-West"),
        telebot.types.InlineKeyboardButton("US-Central", callback_data="US-Central"),
        telebot.types.InlineKeyboardButton("US-East", callback_data="US-East"),
        telebot.types.InlineKeyboardButton("Southamerica", callback_data="Southamerica"),
        telebot.types.InlineKeyboardButton("Asia", callback_data="Asia"))

    bot.send_message(message.chat.id, '🗺 Choose your region', reply_markup=markup)
    print(message.chat.id)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
        
    if call.data in regions:
        bot.answer_callback_query(call.id, f"You chose {call.data}")
        #msg = bot.send_message(call.message.chat.id, show_region_status(get_server_status_raw(), call.data))
        handle_platform(call.message, call.data)

#TODO optimize complexity
    # if call.data in platforms:
    #     bot.answer_callback_query(call.id, f"You chose {call.data}")
    #     msg = bot.send_message(call.message.chat.id, show_platform_status(get_server_status_raw(), call.data))
        

@bot.message_handler()
def handle_platform(message, region):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        telebot.types.InlineKeyboardButton("PC", callback_data="Origin_login"),
        telebot.types.InlineKeyboardButton("Playstation", callback_data="Playstation-Network"),
        telebot.types.InlineKeyboardButton("XBoX", callback_data="Xbox-Live"))

    bot.send_message(message.chat.id, f'{show_region_status(get_server_status_raw(), region)}\n\n 🖱🎮 Choose your platform', reply_markup=markup)

bot.infinity_polling()