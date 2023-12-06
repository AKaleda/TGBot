# coding=windows-1251  
import telebot
import os
from telebot import types

# To set an environment variable> set varname=value (!no spaces before and after the '=' sign)
# To unset an environment variable> , set varname= 
# To see all environment variables> set

# Find @botfather in Telegram, start it and create new bot by command /newbot 
# AKaledaPhotoAudio_bot
# Обращение t.me/AKaledaPhotoAudio_bot
# @botfather will return PRIVATE TOKEN like 6548648010:A...Vpk
# Set environment variable AKaleda_bot_TOKEN by cmd> set AKaleda_bot_TOKEN=6548648010:A...Vpk
# Start python TGBot.py

token = os.getenv('AKaleda_bot_TOKEN')
print(token)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])    # декоратор по обработке команд к телеботу
def start(message):                         # /start
    markup = types.InlineKeyboardMarkup()   # разметка экрана, общее окно
    getCode = types.InlineKeyboardButton(text='See Code', url='https://github.com/AKaleda/TGBot/blob/main/TGBot.py')
    markup.add(getCode)
    bot.send_message(message.from_user.id, "See Code at GitHub", reply_markup = markup) # послать message и ответы получать в этот бот

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) # разрешить resize_keyboard
    btnP = types.KeyboardButton("Pictures")                  # создать button
    btnA = types.KeyboardButton('Audio')                     # создать button
    markup.add(btnP, btnA)                                   # положить на экран
    bot.send_message(message.from_user.id, "Select action", reply_markup=markup) #послать message

@bot.message_handler(content_types=['text'])                 # Контроль входных действий (actions)
def get_text_messages(message):                              # получить сообщение
    if message.text == 'Pictures':
        img = open('photo1.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)    # послать картинку в бот
        img.close()

    if message.text == 'Audio':
        audio = open(r'C:\Windows\Media\Alarm01.wav', 'rb')
        bot.send_audio(message.chat.id, audio)               # послать аудио в бот
        audio.close()

bot.infinity_polling()      # запустить в бесконечный цикл

