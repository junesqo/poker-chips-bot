import telebot
from telebot import types
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

chips = 1000
pot = 0
bet = 0

#lang = 0 - russian, #lang = 1 - english
lang = 0

def diller(message):
    global chips
    global bet

    if message.text is int == False:
        bot.send_message(message.from_user.id, errorinputtext)
    else:
        bet = message.text
        chips = int(chips) - int(bet)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bet_btn = types.KeyboardButton(text=iwon)
        check_btn = types.KeyboardButton(text=check)
        fold_btn = types.KeyboardButton(text=ilose)
        next_turn_btn = types.KeyboardButton(text='')
        markup.add(bet_btn, check_btn, fold_btn)
        bot.send_message(message.from_user.id, yourbet + str(bet), parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, mess)

def win(message):
    global chips
    global pot

    if message.text is int == False:
        bot.send_message(message.from_user.id, errorinputtext)
    else:
        pot = message.text
        chips = int(chips) + int(pot)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        new_game_btn = types.KeyboardButton(text=turn)
        markup.add(new_game_btn)
        if lang == 0:
            yourwin = 'Ваш выигрыш ' + str(pot) + '\nИтого у вас ' + str(chips)
        else:
            yourwin = 'Your winnings ' + str(pot) + '\nIn total you have ' + str(chips)
        bot.send_message(message.from_user.id, yourwin, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, mess)

def lose(message):
    global chips
    global pot

    if message.text is int == False:
        bot.send_message(message.from_user.id, errorinputtext)
    else:
        pot = message.text
        chips = int(chips) - int(pot)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        new_game_btn = types.KeyboardButton(text=turn)
        markup.add(new_game_btn)
        if lang == 0:
            yourloss = 'Ваш проигрыш ' + str(pot) + '\nИтого у вас ' + str(chips)
        else:
            yourloss = 'Your loss ' + str(pot) + '\nIn total you have ' + str(chips)
        bot.send_message(message.from_user.id, yourloss, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, mess)


@bot.message_handler(commands=['language'])
def language(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    russian = types.KeyboardButton('русский')
    english = types.KeyboardButton('english')
    markup.add(russian, english)
    bot.send_message(message.chat.id, 'выберите язык / choose a language', parse_mode='html', reply_markup=markup)

#language settings
if lang == 0:
    errorinputtext = 'Введи цифры!'
    bettext = 'сделать ставку'
    foldtext = 'фолд'
    iwon='я выиграл'
    check='чек'
    ilose='я проиграл'
    yourbetinput='Напишите сумму вашей ставки'
    yourbet='Ваша ставка '
    turn = 'сделать ход'
    yourwininput = 'Напишите сумму вашего выигрыша'
    #yourwin='Ваш выигрыш ' + str(pot) + '\nИтого у вас ' + str(chips)
    #yourloseinput = str(chips)+'\nНапишите сумму вашего проигрыша'
    #yourloss='Ваш проигрыш ' + str(pot) + '\nИтого у вас ' + str(chips)
    nexttext='что будем делать?'

else:
    errorinputtext = 'Write a number'
    bettext = 'bet'
    foldtext = 'fold'
    iwon = 'i won'
    check = 'check'
    ilose = 'i lose'
    yourbetinput='Write your bet'
    yourbet='Your bet '
    turn = 'turn'
    yourwininput = 'Write your win sum'
    nexttext = 'what do you want to do now?'
    #yourwin='Your winnings ' + str(pot) + '\nIn total you have ' + str(chips)
    #yourloseinput = str(chips)+'\nWrite your lose sum'
    #yourloss = 'Your loss ' + str(pot) + '\nIn total you have ' + str(chips)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    if lang == 0:
        btn1 = types.KeyboardButton('сделать ход')
        send_mess = f"<b>Привет {message.from_user.first_name} </b>!\nдавай начнем игру"
    else:
        btn1 = types.KeyboardButton('turn')
        send_mess = f"<b>Hello {message.from_user.first_name} </b>!\nlet's start a game"
    markup.add(btn1)
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, mess)






@bot.message_handler(content_types=['text'])

def switch(message):
    global lang
    if message.text == 'русский':
        lang = 0
    else:
        lang = 1
    bot.register_next_step_handler(message, win)

def mess(message):

    global chips
    global bet
    get_message_bot = message.text.lower()

    #сделать ход
    if get_message_bot == 'сделать ход' or get_message_bot == 'turn':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bet_btn = types.KeyboardButton(text=bettext)
        check_btn = types.KeyboardButton(text=check)
        fold_btn = types.KeyboardButton(text=foldtext)
        markup.add(bet_btn, check_btn, fold_btn)
        bot.send_message(message.chat.id, nexttext, parse_mode='html', reply_markup=markup)

    elif get_message_bot == 'сделать ставку' or get_message_bot == 'bet':
        bot.send_message(message.chat.id, str(chips) + yourbetinput, parse_mode='html')
        bot.register_next_step_handler(message, diller)

    elif get_message_bot == "я выиграл" or get_message_bot == 'i won':
        bet = 0
        bot.send_message(message.chat.id, str(chips) + '\n' + yourwininput, parse_mode='html')
        bot.register_next_step_handler(message, win)

    elif get_message_bot == 'чек' or get_message_bot == 'check':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bet_btn = types.KeyboardButton(text=bettext)
        check_btn = types.KeyboardButton(text=check)
        fold_btn = types.KeyboardButton(text=foldtext)
        win_btn = types.KeyboardButton(text=iwon)
        lose_btn = types.KeyboardButton(text=ilose)
        markup.row(bet_btn, check_btn, fold_btn)
        markup.row(win_btn, lose_btn)
        bot.send_message(message.chat.id, nexttext, parse_mode='html', reply_markup=markup)

    #проигрыш
    elif get_message_bot == "фолд" or get_message_bot == "я проиграл" or get_message_bot == 'fold' or get_message_bot == 'i lose':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bet = 0
        new_game = types.KeyboardButton(text='начать игру')
        markup.add(new_game)
        if lang == 0:
            yourloseinput = str(chips) + '\nНапишите сумму вашего проигрыша'
        else:
            yourloseinput = str(chips) + '\nWrite your lose sum'
        bot.send_message(message.chat.id, yourloseinput, parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, lose)

    #else:

bot.polling(none_stop=True, interval=0)
