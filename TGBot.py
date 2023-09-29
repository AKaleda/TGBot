# coding=windows-1251  
import telebot
import os
from telebot import types

# To set an environment variable> set varname=value (!no spaces before and after the '=' sign)
# To unset an environment variable> , set varname= 
# To see all environment variables> set

# Find @botfather in Telegram, start it and create new bot by command /newbot
# @botfather will return TOKEN like 6548648010:A...Vpk
# Set environment variable AKaleda_bot_TOKEN by cmd> set AKaleda_bot_TOKEN=6548648010:A...Vpk
# Start python TGBot.py

token = os.getenv('AKaleda_bot_TOKEN')
print(token)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    getCode = types.InlineKeyboardButton(text='See Code', url='https://github.com/AKaleda/TGBot/blob/main/TGBot.py')
    markup.add(getCode)
    bot.send_message(message.from_user.id, "See Code at GitHub", reply_markup = markup)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btnP = types.KeyboardButton("Pictures")
    btnA = types.KeyboardButton('Audio')
    markup.add(btnP, btnA)
    bot.send_message(message.from_user.id, "Select action", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Pictures':
        #tb.send_chat_action(message.chat.id, 'upload_photo')
        img = open('photo1.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        img.close()

    if message.text == 'Audio':
        audio = open(r'C:\Windows\Media\Alarm01.wav', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()

bot.infinity_polling()

