from __future__ import division
import telebot
from math import ceil
import random
import json
import time

bot = telebot.TeleBot("1881287441:AAHo_PE__wRrzRiyITwVotWCMEY2T4hCIxQ", parse_mode=None)
with open('file.json') as json_data:
    data = json.load(json_data,)
#total = list (data)
# sendMessage
#def mes ():
 #   random.choice(data)
  #  return (mes)
betweenDLs = 10 # minutes
totalTime = 2*60 # minutes
for i in range(int(ceil(totalTime/betweenDLs))):
    bot.send_message(chat_id=-1001556934353, text=random.choice(data))
    time.sleep(betweenDLs*60)


bot.polling(none_stop=True, interval=0)

