import dotenv
import telebot
import os
from Utils import RESTreq as req

dotenv.load_dotenv()
API_KEY_TELEGRAM = os.environ.get('API_KEY_TELEGRAM')

bot = telebot.TeleBot(API_KEY_TELEGRAM)

print(req.getMapRotation())

#@bot.message_handler(content_types=['text'])
#def handle_command_adminwindow(message):
#    global msg_count
#    current_time = datetime.datetime.now().hour
#    if (current_time < 6):
#        msg_count = msg_count + 1
#         if (msg_count == 10):
        
#             bot.send_message(chat_id=message.chat.id,
#                             text="Reply service is unavailable during the midnight",
#                             parse_mode='HTML')
#     else:
    


# bot.infinity_polling()