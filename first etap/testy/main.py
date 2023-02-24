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
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rock = types.KeyboardButton('Rock')
    paper = types.KeyboardButton('Scissors')
    scissors = types.KeyboardButton('Paper')
    markup.add(rock, paper, scissors)
    bot.send_message(message.chat.id, 'Click on the button', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    import random
    import json
    with open('users.json', 'w') as f:
        score = {}
        bot1 = 0
        user = 0
        draw = 0
        score["Bot"] = bot1
        score[""]
    test_list = ['Rock', 'Scissors', 'Paper']
    random_index = random.randrange(len(test_list))
    bot.send_message(message.chat.id, test_list[random_index], parse_mode='html')
    if message.text == 'Paper' and test_list[random_index] == 'Paper':
        bot.send_message(message.chat.id, "Draw", parse_mode='html')
        draw = draw + 1
        mes = f"Draws: {draw}\n{message.from_user.first_name}: {user}\nBot: {bot1}"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == 'Paper' and test_list[random_index] == 'Rock':
        bot.send_message(message.chat.id, "You win", parse_mode='html')
        user = user + 1
        mes = f"Draws: {draw}\n{message.from_user.first_name}: {user}\nBot: {bot1}"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == 'Paper' and test_list[random_index] == 'Scissors':
        bot.send_message(message.chat.id, "You lose", parse_mode='html')
        bot1 = bot1 + 1
        mes = f"Draws: {draw}\n{message.from_user.first_name}: {user}\nBot: {bot1}"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    if message.text == 'Rock' and test_list[random_index] == 'Paper':
        bot.send_message(message.chat.id, "You lose", parse_mode='html')
        bot1 = bot1 + 1
        mes = f"Draws: {draw}\n{message.from_user.first_name}: {user}\nBot: {bot1}"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == 'Rock' and test_list[random_index] == 'Rock':
        bot.send_message(message.chat.id, "Draw", parse_mode='html')
        draw = draw + 1
        mes = f"Draws: {draw}\n{message.from_user.first_name}: {user}\nBot: {bot1}"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == 'Rock' and test_list[random_index] == 'Scissors':
        bot.send_message(message.chat.id, "You win", parse_mode='html')
        user = user + 1
        mes = f"Draws: {draw}\n{message.from_user.first_name}: {user}\nBot: {bot1}"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    if message.text == 'Scissors' and test_list[random_index] == 'Paper':
        bot.send_message(message.chat.id, "You win", parse_mode='html')
        user = user + 1
        mes = f"Draws: {draw}\n{message.from_user.first_name}: {user}\nBot: {bot1}"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == 'Scissors' and test_list[random_index] == 'Rock':
        bot.send_message(message.chat.id, "You lose", parse_mode='html')
        bot1 = bot1 + 1
        mes = f"Draws: {draw}\n{message.from_user.first_name}: {user}\nBot: {bot1}"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == 'Scissors' and test_list[random_index] == 'Scissors':
        bot.send_message(message.chat.id, "Draw", parse_mode='html')
        draw = draw + 1
        mes = f"Draws: {draw}\n{message.from_user.first_name}: {user}\nBot: {bot1}"
        bot.send_message(message.chat.id, mes, parse_mode='html')


bot.polling(none_stop=True)
