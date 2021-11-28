import telebot
from telebot import types

token = ''
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", 'Расписание занятий', 'ДЗ', '/news', '/logo')
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею отправлять ссылку на официальный сайт МТУСИ, на расписание занятий '
                                      'БВТ2106, на домашнее задание, на новости и показывать логотип МТУСИ ')

@bot.message_handler(commands=['news'])
def start_message_1(message):
    if message.text == '/news':
        bot.send_message(message.chat.id, 'https://t.me/infomoscow24')

@bot.message_handler(commands=['logo'])
def start_message_2(message):
    if message.text == '/logo':
        bot.send_photo(message.chat.id, photo='https://upload.wikimedia.org/wikipedia/ru/7/7b/Mtuci_logo.png',
                       caption='MTUCI')



@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text == "Расписание занятий":
        bot.send_message(message.chat.id, '[Расписание](https://disk.yandex.ru/i/BxcUZY1OKjK0GQ)', parse_mode='Markdown')
    elif message.text == "ДЗ":
        bot.send_message(message.chat.id, '[Домашнее задание](https://docs.google.com/spreadsheets/d/1lFbNb2-pQXgbf66b-e6lfxqr-O51JNrMzclZkyUV2p4/edit#gid=0)', parse_mode='Markdown')




bot.polling(non_stop=True)
