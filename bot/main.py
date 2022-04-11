import dotenv
import telebot
import os
import requests

dotenv.load_dotenv()
API_KEY = os.environ.get('API_KEY')
os.environ['TOKEN'] = '<ADD_BEARER_TOKEN>'

bot = telebot.TeleBot(API_KEY)

def getTweet():
    twurl -X GET "/labs/2/tweets/1138505981460193280?expansions=attachments.media_keys&tweet.fields=created_at,author_id,lang,source,public_metrics,context_annotations,entities"


        
@bot.message_handler(content_types=['text'])
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