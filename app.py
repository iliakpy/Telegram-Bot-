import telebot
from config import keys, TOKEN
from utils import CryptoConverter, ConvertionException

bot = telebot.TeleBot (TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду боту в следущем формате:\n<имя валюты>  \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split (' ')

    if len (values) != 3:
        raise ConvertionException ('Слишком много параметров')

    quote, base, amount = values
    total_base = CryptoConverter.convert(quote, base, amount)

    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Красивое фото )))')

@bot.message_handler(content_types=['voice', ])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, 'У вас красивый голос )))')


bot.polling()
