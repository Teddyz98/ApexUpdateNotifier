import dotenv
import telebot
import os
from utils import get_battle_royale_current_map, get_map_informations, get_server_status_raw, show_region_status, is_platform_up, select_platform, get_user_info

dotenv.load_dotenv()
API_KEY_TELEGRAM = os.environ.get('API_KEY_TELEGRAM')
print(API_KEY_TELEGRAM)
bot = telebot.TeleBot(API_KEY_TELEGRAM)
print(bot)

commands = {  # command description used in the "help" command
    'start'       : '\tGet used to the bot',
    'help'        : '\tShow available commands',
    'map'         : '\tCurrent and the next map',
    'server'      : '\tGet the server status'
}

regions = ["EU-West", "EU-East","US-West","US-East", "Southamerica", "Asia"]
platforms = ["Origin_login","Playstation-Network","Xbox-Live"]
platforms_stats = ['PC','PS4','X1']

@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, """
        Hi there 👋🏼, I am Apex Update Notifier Bot. I notify you with some useful informations about Apex Legends!
        """)

@bot.message_handler(commands=['help'])
def command_help(message):
    help_text = "⚙️ Commands: \n\n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "• /" + key + " - "
        help_text += commands[key] + "\n"
    bot.send_message(message.chat.id, help_text)  # send the generated help page

@bot.message_handler(commands=['map'])
def map(message):
    bot.send_message(message.chat.id, get_map_informations(get_battle_royale_current_map()), parse_mode='MarkdownV2')

@bot.message_handler(commands=['server'])
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

@bot.callback_query_handler(lambda call: call.data in regions)
def callback_query_servers(call):
        
    bot.answer_callback_query(call.id, f"You chose {call.data}")
    bot.send_message(call.message.chat.id, f'{show_region_status(get_server_status_raw(), call.data)}\n\n{select_platform(get_server_status_raw(), call.data)}')

@bot.message_handler(commands=['player'])
def player_stats(message):

    username = ' '.join(message.text.split(' ')[1:])

    markup = telebot.types.InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        telebot.types.InlineKeyboardButton("PC", callback_data="PC"),
        telebot.types.InlineKeyboardButton("PS4", callback_data="PS4"),
        telebot.types.InlineKeyboardButton("Xbox", callback_data="X1")
    )

    bot.send_message(message.chat.id, f'Choose your platform {username}', reply_markup=markup) #the "username" in the message is necessary to pass it to the query handler

@bot.callback_query_handler(lambda call: call.data in platforms_stats)
def callback_query_platforms(call):

    print(call)
    bot.answer_callback_query(call.id, f"You chose {call.data}")
    username = call.message.text.split()[-1] #get last word
    bot.send_message(call.message.chat.id, get_user_info(username, call.data), parse_mode='MarkdownV2')
        
bot.infinity_polling()