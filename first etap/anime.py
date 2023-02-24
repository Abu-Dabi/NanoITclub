import telebot
from telebot import types

bot = telebot.TeleBot('6046257454:AAHRqEgaHuEQIaRvWyJY_p-Y7I8C5RiL8AY')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, 'Best anime?', parse_mode='html')


@bot.message_handler(commands=['watch'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    tokyo_avengers = types.KeyboardButton('/Tokyo_avengers')
    vinland_saga = types.KeyboardButton('/Vinland_saga')
    my_hero_academia = types.KeyboardButton('/My_hero_academia')
    blue_lock = types.KeyboardButton('/Blue_lock')
    markup.add(tokyo_avengers, vinland_saga, my_hero_academia, blue_lock)
    bot.send_message(message.chat.id, 'Click on the button', reply_markup=markup)


@bot.message_handler(commands=['Tokyo_avengers'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Go to watch anime", url="https://jut.su/tokyo-reveengers/"))
    bot.send_message(message.chat.id, 'Go to the site', reply_markup=markup)


@bot.message_handler(commands=['Vinland_saga'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Go to watch anime", url="https://jut.su/vinland-saga/"))
    bot.send_message(message.chat.id, 'Go to the site', reply_markup=markup)


@bot.message_handler(commands=['My_hero_academia'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("Go to watch anime", url="https://jut.su/boku-hero-academia/"))
    bot.send_message(message.chat.id, 'Go to the site', reply_markup=markup)


@bot.message_handler(commands=['Blue_lock'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Go to watch anime", url="https://jut.su/blue-lock/"))
    bot.send_message(message.chat.id, 'Go to the site', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'One-piece':
        bot.send_message(message.chat.id, 'True! One-piece the best anime', parse_mode='html')
    else:
        bot.send_message(message.chat.id, "False! Click on /watch to go watch best animes", parse_mode='html')


bot.polling(none_stop=True)