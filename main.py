import telebot
from telebot import types
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

chips=1000

pot=0
bet=0

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('сделать ход')
    markup.add(btn1)
    send_mess = f"<b>Привет {message.from_user.first_name} </b>!\nдавай начнем игру"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

def diller(message):
    global chips
    global bet
    get_bet = message.text.strip()
    if message.text is int == False:
        bot.send_message(message.from_user.id, 'Введи цифры!')
    else:
        bet = message.text
        chips = int(chips) - int(bet)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bet_btn = types.KeyboardButton(text='я выиграл')
        check_btn = types.KeyboardButton(text='чек')
        fold_btn = types.KeyboardButton(text='я проиграл')
        next_turn_btn = types.KeyboardButton(text='')
        markup.add(bet_btn, check_btn, fold_btn)

        bot.send_message(message.from_user.id, 'Ваша ставка ' + bet, parse_mode='html', reply_markup=markup)

        bot.register_next_step_handler(message, mess)

def win(message):
    global chips
    global pot
    get_bet = message.text.strip()
    if message.text is int == False:
        bot.send_message(message.from_user.id, 'Введи цифры!')
    else:
        pot = message.text
        chips = int(chips) + int(pot)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        new_game_btn = types.KeyboardButton(text='сделать ход')
        markup.add(new_game_btn)
        bot.send_message(message.from_user.id, 'Ваш выигрыш ' + str(pot) + '\nИтого у вас ' + str(chips), parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, mess)

def lose(message):
    global chips
    global pot
    if message.text is int == False:
        bot.send_message(message.from_user.id, 'Введи цифры!')
    else:
        pot = message.text
        chips = int(chips) - int(pot)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        new_game_btn = types.KeyboardButton(text='сделать ход')
        markup.add(new_game_btn)
        bot.send_message(message.from_user.id, 'Ваш проигрыш ' + str(pot) + '\nИтого у вас ' + str(chips), parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, mess)

@bot.message_handler(content_types=['text'])
def mess(message):
    global chips
    global bet
    get_message_bot = message.text.strip().lower()

    #сделать ход
    if get_message_bot == 'сделать ход' or get_message_bot == 'что будем делать?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bet_btn = types.KeyboardButton(text='сделать ставку')
        check_btn = types.KeyboardButton(text='чек')
        fold_btn = types.KeyboardButton(text='фолд')
        markup.add(bet_btn, check_btn, fold_btn)
        final_message = "что будем делать?"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    elif get_message_bot == "сделать ставку":
        #markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        #bet_btn = types.KeyboardButton(text='ааа')
        #check_btn = types.KeyboardButton(text='чек')
        #fold_btn = types.KeyboardButton(text='ббб')
        #markup.add(bet_btn, check_btn, fold_btn)
        bot.send_message(message.chat.id, str(chips)+'\nНапишите сумму вашей ставки', parse_mode='html')
        bot.register_next_step_handler(message, diller)

    elif get_message_bot == "я выиграл":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bet = 0
        fold_btn = types.KeyboardButton(text='начать игру')
        markup.add(fold_btn)
        bot.send_message(message.chat.id, str(chips)+'\nНапишите сумму вашего выигрыша', parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, win)

    elif get_message_bot == 'чек':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bet_btn = types.KeyboardButton(text='сделать ставку')
        check_btn = types.KeyboardButton(text='чек')
        fold_btn = types.KeyboardButton(text='фолд')
        win_btn = types.KeyboardButton(text='я выиграл')
        lose_btn = types.KeyboardButton(text='я проиграл')
        markup.row(bet_btn, check_btn, fold_btn)
        markup.row(win_btn, lose_btn)
        final_message = "что будем делать?"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

    #проигрыш
    elif get_message_bot == "фолд" or get_message_bot == "я проиграл":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bet = 0
        fold_btn = types.KeyboardButton(text='начать игру')
        markup.add(fold_btn)
        bot.send_message(message.chat.id, str(chips)+'\nНапишите сумму вашего проигрыша', parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, lose)

    #else:

bot.polling(none_stop=True, interval=0)
