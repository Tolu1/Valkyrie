import telebot
import time
import os
from dotenv import load_dotenv
from Interactive.core.models import Dialogflow
from Interactive.misc import Templates

load_dotenv()

API_KEY = os.getenv('TELEGRAM_API_KEY')
bot = telebot.TeleBot(API_KEY)
dflow = Dialogflow('./private_key_valkyrie.json')

command_char = '!'

@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id, 'Welcome to BotHub ╲ʕ·ᴥ·　╲ʔ')

@bot.message_handler(commands=['help'])
def help(message):
  bot.send_message(message.chat.id, 'Helpboard coming soon📌')

@bot.message_handler(func=lambda m: True, content_types=['text', 'new_chat_members'])
def main(message):
  print(message)

  # ======================================================================= # 
  #                           CODE FOR PRIVATE CHAT                         #
  # ======================================================================= #

  # Regular texting
  if message.chat.type == 'private':
    # bot.send_message(message.chat.id, "I'm still under construction⚠️ but I know this is a private message")
    bot.send_message(message.chat.id, dflow.interact(message.text))
  

  # ======================================================================= # 
  #                            CODE FOR GROUP CHAT                          #
  # ======================================================================= #

  # Regular texting
  if message.chat.type == 'group':
    if message.content_type == 'text':
      # if message.text[0] == command_char:
        if message.entities is None:
          bot.send_message(message.chat.id, "I'm still under construction⚠️ but I know this is a group message")
        else:
          for entity in message.entities:
            if entity.type == 'mention' and message.text[entity.offset:entity.length] == '@' + bot.get_me().username:
              # bot.send_message(message.chat.id, "I'm still under construction⚠️ but I know someone mentioned my name just now")
              print(message.text.replace(message.text[entity.offset:entity.length], ''))
              bot.send_message(message.chat.id, dflow.interact(message.text.replace(message.text[entity.offset:entity.length], '')))
              break

    # New group member event
    if message.content_type == 'new_chat_members':
      for member in message.new_chat_members:
        if member.username is not None:
          name = f'@{member.username}'
        else:
          name = f'{member.first_name}'
        
        bot.send_message(message.chat.id, Templates.get_random_new_group_member_welcome_message()[int(random.randint(0, len(welcome_messages)-1))].replace('[username]', name))


# Poll Telegram servers till eternity
print('Polling Telegram servers for new messages...till Jesus comes')
while True:
  try:
    bot.polling()
  except Exception as e:
    print(e)
    time.sleep(10)