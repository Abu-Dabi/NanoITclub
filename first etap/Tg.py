import telebot
from telebot import types

bot = telebot.TeleBot('6046257454:AAHRqEgaHuEQIaRvWyJY_p-Y7I8C5RiL8AY')


@bot.message_handler(commands=['start'])
def start(message):
    mess = "Welcome to the ABU_bot"
    bot.send_message(message.chat.id, mess, parse_mode='html')
    mes = "Write /help to get information"
    bot.send_message(message.chat.id, mes, parse_mode='html')


@bot.message_handler(commands=['help'])
def website(message):
    markup = types. ReplyKeyboardMarkup(resize_keyboard=True)
    hello = types.KeyboardButton('Hello')
    id1 = types.KeyboardButton('ID')
    photo = types.KeyboardButton('Photo')
    anime = types.KeyboardButton('/Anime')
    markup.add(hello, id1, photo, anime)
    bot.send_message(message.chat.id, 'Click on the button', reply_markup=markup)


@bot.message_handler(commands=['Anime'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Go to watch anime", url="https://jut.su/oneepiece/"))
    bot.send_message(message.chat.id, 'Go to the site', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, F'Hi, <b>{message.from_user.first_name}</b>', parse_mode='html')
    elif message.text == 'ID':
        bot.send_message(message.chat.id, f"Your ID:{message.from_user.id}", parse_mode='html')
    elif message.text == 'Photo':
        photo = open('img.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'I dont understand you, write /help', parse_mode='html')


bot.polling(none_stop=True)
