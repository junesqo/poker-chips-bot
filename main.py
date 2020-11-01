import telebot
from telebot import types
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
chips = 1000

<<<<<<< HEAD
pot = 0
bet = 0


# this is a start command
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('сделать ход')
    btn2 = types.KeyboardButton('указать количество фишек')
    markup.add(btn1, btn2)
    send_mess = f"<b>Привет {message.from_user.first_name} </b>" \
        f"!\nдавай начнем подсчет твоих фишек"
    bot.send_message(
        message.chat.id, send_mess, parse_mode='html', reply_markup=markup
    )
=======
chips = 1000
pot = 0
bet = 0

#lang = 0 - russian, #lang = 1 - english
lang = 0
>>>>>>> 557f09512dd692c872da2751de43491072b5e06e


# this is a function to get a bet
def diller(message):
    global chips
    global bet
<<<<<<< HEAD
    try:
=======

    if message.text is int == False:
        bot.send_message(message.from_user.id, errorinputtext)
    else:
>>>>>>> 557f09512dd692c872da2751de43491072b5e06e
        bet = message.text
        bet = int(bet)
        chips = int(chips) - int(bet)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
<<<<<<< HEAD
        bet_btn = types.KeyboardButton(text='я выиграл')
        check_btn = types.KeyboardButton(text='чек')
        fold_btn = types.KeyboardButton(text='я проиграл')
        markup.add(bet_btn, check_btn, fold_btn)
        yourbet = 'Ваша ставка ' + bet
        bot.send_message(
            message.from_user.id, yourbet, reply_markup=markup
        )

        bot.register_next_step_handler(message, mess)
    except ValueError:
        bot.send_message(message.from_user.id, 'Вы ввели не цифры')


# this is a function to edit a number of chips player wants to play
def chipscount(message):
    global chips
    try:
        chips = message.text
        chips = int(chips)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        new_game_btn = types.KeyboardButton(text='сделать ход')
        markup.add(new_game_btn)
        cctext = 'Итого у вас ' + str(chips)
        bot.send_message(message.from_user.id, cctext, reply_markup=markup)
=======
        bet_btn = types.KeyboardButton(text=iwon)
        check_btn = types.KeyboardButton(text=check)
        fold_btn = types.KeyboardButton(text=ilose)
        next_turn_btn = types.KeyboardButton(text='')
        markup.add(bet_btn, check_btn, fold_btn)
        bot.send_message(message.from_user.id, yourbet + str(bet), parse_mode='html', reply_markup=markup)
>>>>>>> 557f09512dd692c872da2751de43491072b5e06e
        bot.register_next_step_handler(message, mess)
    except ValueError:
        bot.send_message(message.from_user.id, 'Вы ввели не цифры')


# win function to count player's winnings
def win(message):
    global chips
    global pot
<<<<<<< HEAD
    try:
=======

    if message.text is int == False:
        bot.send_message(message.from_user.id, errorinputtext)
    else:
>>>>>>> 557f09512dd692c872da2751de43491072b5e06e
        pot = message.text
        pot = int(pot)
        chips = int(chips) + int(pot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        new_game_btn = types.KeyboardButton(text=turn)
        markup.add(new_game_btn)
<<<<<<< HEAD
        wintext = 'Ваш выигрыш ' + str(pot) + '\nИтого у вас ' + str(chips)
        bot.send_message(
            message.from_user.id, wintext, reply_markup=markup
        )
=======
        if lang == 0:
            yourwin = 'Ваш выигрыш ' + str(pot) + '\nИтого у вас ' + str(chips)
        else:
            yourwin = 'Your winnings ' + str(pot) + '\nIn total you have ' + str(chips)
        bot.send_message(message.from_user.id, yourwin, parse_mode='html', reply_markup=markup)
>>>>>>> 557f09512dd692c872da2751de43491072b5e06e
        bot.register_next_step_handler(message, mess)
    except ValueError:
        bot.send_message(message.from_user.id, 'Вы ввели не цифры')


# lose function to count player's loss
def lose(message):
    global chips
    global pot
<<<<<<< HEAD
    try:
=======

    if message.text is int == False:
        bot.send_message(message.from_user.id, errorinputtext)
    else:
>>>>>>> 557f09512dd692c872da2751de43491072b5e06e
        pot = message.text
        pot = int(pot)
        chips = int(chips) - int(pot)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        new_game_btn = types.KeyboardButton(text=turn)
        markup.add(new_game_btn)
<<<<<<< HEAD
        bot.send_message(message.from_user.id, 'Ваш проигрыш ' + str(pot) +
                         '\nИтого у вас ' + str(chips),
                         parse_mode='html', reply_markup=markup)
=======
        if lang == 0:
            yourloss = 'Ваш проигрыш ' + str(pot) + '\nИтого у вас ' + str(chips)
        else:
            yourloss = 'Your loss ' + str(pot) + '\nIn total you have ' + str(chips)
        bot.send_message(message.from_user.id, yourloss, parse_mode='html', reply_markup=markup)
>>>>>>> 557f09512dd692c872da2751de43491072b5e06e
        bot.register_next_step_handler(message, mess)
    except ValueError:
        bot.send_message(message.from_user.id, 'Вы ввели не цифры')


<<<<<<< HEAD
# there is where all turns
=======

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






>>>>>>> 557f09512dd692c872da2751de43491072b5e06e
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

<<<<<<< HEAD
    # сделать ход
    if get_message_bot == 'сделать ход':
=======
    #сделать ход
    if get_message_bot == 'сделать ход' or get_message_bot == 'turn':
>>>>>>> 557f09512dd692c872da2751de43491072b5e06e
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bet_btn = types.KeyboardButton(text=bettext)
        check_btn = types.KeyboardButton(text=check)
        fold_btn = types.KeyboardButton(text=foldtext)
        markup.add(bet_btn, check_btn, fold_btn)
<<<<<<< HEAD
        final_message = "что будем делать?"
        bot.send_message(
            message.chat.id, final_message, reply_markup=markup
        )

    elif get_message_bot == 'указать количество фишек':
        chipsinputtext = 'введите ваше общее количество фишек'
        bot.send_message(message.chat.id, chipsinputtext)
        bot.register_next_step_handler(message, chipscount)

    elif get_message_bot == "сделать ставку":
        bettext = str(chips)+'\nНапишите сумму вашей ставки'
        bot.send_message(message.chat.id, bettext)
        bot.register_next_step_handler(message, diller)

    elif get_message_bot == "я выиграл":
        bet = 0
        iwon = str(chips)+'\nНапишите сумму вашего выигрыша'
        bot.send_message(message.chat.id, iwon)
=======
        bot.send_message(message.chat.id, nexttext, parse_mode='html', reply_markup=markup)

    elif get_message_bot == 'сделать ставку' or get_message_bot == 'bet':
        bot.send_message(message.chat.id, str(chips) + yourbetinput, parse_mode='html')
        bot.register_next_step_handler(message, diller)

    elif get_message_bot == "я выиграл" or get_message_bot == 'i won':
        bet = 0
        bot.send_message(message.chat.id, str(chips) + '\n' + yourwininput, parse_mode='html')
>>>>>>> 557f09512dd692c872da2751de43491072b5e06e
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
<<<<<<< HEAD
        final_message = "что будем делать?"
        bot.send_message(
            message.chat.id, final_message, reply_markup=markup
        )

    # проигрыш
    elif get_message_bot == "фолд" or get_message_bot == "я проиграл":
        bet = 0
        losetext = str(chips)+'\nНапишите сумму вашего проигрыша'
        bot.send_message(message.chat.id, losetext)
=======
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
>>>>>>> 557f09512dd692c872da2751de43491072b5e06e
        bot.register_next_step_handler(message, lose)


# to continue bot working
bot.polling(none_stop=True, interval=0)
