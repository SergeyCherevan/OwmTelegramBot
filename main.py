
import telebot
import pyowm
from pyowm.utils.config import get_default_config


# никогда не делайте так: всегда храните токены  в отдельном файле с .gitignore
bot = telebot.TeleBot('1840232772:AAF4PGhwUlOqPT2PIaq9agD_NT2G1DphcFE')

config_dict = get_default_config()
config_dict['language'] = 'ru' 

owm = pyowm.OWM('72c54c1bd6c687fc349399740978ac29', config_dict)
mgr = owm.weather_manager()



@bot.message_handler(content_types=['text'])
def send_welcome(message):

    place = message.text

    try:
        observation = mgr.weather_at_place(place)

    except:
        bot.reply_to(message, "К сожалению, город не найден. Попродуйте другое название")
        return

    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + place + " сейчас " + w.detailed_status + "\n";
    answer += "Температура около " + str(temp) + "℃."

    bot.reply_to(message, answer)
    


bot.polling( none_stop=True )