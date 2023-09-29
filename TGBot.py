# coding=windows-1251  
import telebot
import os
from telebot import types

# To set an environment variable> set varname=value (!no spaces before and after the '=' sign)
# To unset an environment variable> , set varname= 
# To see all environment variables> set

# ����� @botfather � Telegram, ��������� ��� � ������� bot �������� /newbot
# @botfather ��������� TOKEN ���� 6548648010:A...Vpk
# ���������� ���������� ��������� �������� � cmd> set AKaleda_bot_TOKEN=6548648010:A...Vpk
# ��������� cmd> python TGBot.py

token = os.getenv('AKaleda_bot_TOKEN')
print(token)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("�������������")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "������! � ���� ���-��������!", reply_markup=markup)

#def send_welcome(message):
#	bot.reply_to(message, "Good day, ��� ����?")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '�������������':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #�������� ����� ������
        btn1 = types.KeyboardButton('��� ����� ������� �� �����?')
        btn2 = types.KeyboardButton('������� �����')
        btn3 = types.KeyboardButton('������ �� ���������� ����������')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '������� ������������ ��� ������', reply_markup=markup) #����� ����


    elif message.text == '��� ����� ������� �� �����?':
        bot.send_message(message.from_user.id, '�� ������ ������ ����, ��� ��������� ����������, �, ���� �� ������, ���������� � �������� ����� �����, ��� �� �������� ���������, ����������� � �������. � ���������� ������������ ��� �� �����������. ���� � ������ ���-�� �� ���, ��� �������� ��� ����������.\n \n������ ����� ����� ��������� �� ' + '[������](https://habr.com/ru/sandbox/start/)', parse_mode='Markdown')

    elif message.text == '������� �����':
        bot.send_message(message.from_user.id, '��������� ������� ����� �� ������ �� ' + '[������](https://habr.com/ru/docs/help/rules/)', parse_mode='Markdown')

    elif message.text == '������ �� ���������� ����������':
        bot.send_message(message.from_user.id, '�������� ��� ������ �� ���������� ���������� ��������� �� ' + '[������](https://habr.com/ru/docs/companies/design/)', parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()

