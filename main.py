import telebot
from telebot import types
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
chips = 1000

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


# this is a function to get a bet
def diller(message):
    global chips
    global bet
    try:
        bet = message.text
        bet = int(bet)
        chips = int(chips) - int(bet)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
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
        bot.register_next_step_handler(message, mess)
    except ValueError:
        bot.send_message(message.from_user.id, 'Вы ввели не цифры')


# win function to count player's winnings
def win(message):
    global chips
    global pot
    try:
        pot = message.text
        pot = int(pot)
        chips = int(chips) + int(pot)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        new_game_btn = types.KeyboardButton(text='сделать ход')
        markup.add(new_game_btn)
        wintext = 'Ваш выигрыш ' + str(pot) + '\nИтого у вас ' + str(chips)
        bot.send_message(
            message.from_user.id, wintext, reply_markup=markup
        )
        bot.register_next_step_handler(message, mess)
    except ValueError:
        bot.send_message(message.from_user.id, 'Вы ввели не цифры')


# lose function to count player's loss
def lose(message):
    global chips
    global pot
    try:
        pot = message.text
        pot = int(pot)
        chips = int(chips) - int(pot)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        new_game_btn = types.KeyboardButton(text='сделать ход')
        markup.add(new_game_btn)
        bot.send_message(message.from_user.id, 'Ваш проигрыш ' + str(pot) +
                         '\nИтого у вас ' + str(chips),
                         parse_mode='html', reply_markup=markup)
        bot.register_next_step_handler(message, mess)
    except ValueError:
        bot.send_message(message.from_user.id, 'Вы ввели не цифры')


# there is where all turns
@bot.message_handler(content_types=['text'])
def mess(message):
    global chips
    global bet
    get_message_bot = message.text.strip().lower()

    # сделать ход
    if get_message_bot == 'сделать ход':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        bet_btn = types.KeyboardButton(text='сделать ставку')
        check_btn = types.KeyboardButton(text='чек')
        fold_btn = types.KeyboardButton(text='фолд')
        markup.add(bet_btn, check_btn, fold_btn)
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
        bot.send_message(
            message.chat.id, final_message, reply_markup=markup
        )

    # проигрыш
    elif get_message_bot == "фолд" or get_message_bot == "я проиграл":
        bet = 0
        losetext = str(chips)+'\nНапишите сумму вашего проигрыша'
        bot.send_message(message.chat.id, losetext)
        bot.register_next_step_handler(message, lose)


# to continue bot working
bot.polling(none_stop=True, interval=0)
