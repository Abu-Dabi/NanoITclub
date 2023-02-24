import telebot
from telebot import types

bot = telebot.TeleBot('6046257454:AAHRqEgaHuEQIaRvWyJY_p-Y7I8C5RiL8AY')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Wow, very cool photo')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Go to website", url="https://www.youtube.com"))
    bot.send_message(message.chat.id, 'Go to the site', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types. ReplyKeyboardMarkup(resize_keyboard=True)
    hello = types.KeyboardButton('Hello')
    id1 = types.KeyboardButton('ID')
    photo = types.KeyboardButton('Photo')
    markup.add(hello, id1, photo)
    bot.send_message(message.chat.id, 'Click on the button', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'Hi', parse_mode='html')
    elif message.text == 'ID':
        bot.send_message(message.chat.id, f"Your ID:{message.from_user.id}", parse_mode='html')
    elif message.text == 'Photo':
        photo = open('img.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'I dont understand you', parse_mode='html')


bot.polling(none_stop=True)
