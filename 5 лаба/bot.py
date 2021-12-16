import telebot

token = '5020404257:AAG2csBAtGtpUBYIn_ajPvUPWUfrZygMawU'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Да', 'Нет')
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать погоду?', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Это очень хорошо! Информация ниже!')
        bot.send_message(message.chat.id, 'Погода на сегодня -2°C, температура для зимы приемлима.')
        bot.send_message(message.chat.id, 'Погода на завтра -11°C, одевайтесь теплее!')
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Хорошо! Возвращайся, когда понадобится информация о погоде!')
    elif message.text.lower() == '/help':
        bot.send_message(message.chat.id, 'Напиши /start')
    else:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/start', '/help')
        bot.send_message(message.chat.id, 'Я не понимаю тебя, давай начнем заново! Нажми /start', reply_markup=keyboard)


bot.polling()
