import COVID19Py
import telebot
from telebot import types

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('5394923070:AAEl8B9ITKyBkslldGwjwFOx-thHH6ds3g0')


@bot.message_handler(commands=['start'])
def start(messege):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.InlineKeyboardButton("Во всем мире")
    btn2 = types.InlineKeyboardButton("Россия")
    btn3 = types.InlineKeyboardButton("США")
    markup.add(btn1, btn2, btn3)
    send_mess = f"<b>Привет {messege.from_user.first_name}!</b>\nВведите страну"
    bot.send_message(messege.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(messege):
    final_message = ""
    get_message_bot = messege.text.strip().lower()
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n" \
                        f"<b>Заболевшие: </b>{location['confirmed']}\n" \
                        f"<b>Умершие: </b>{location['deaths']}\n"

    if final_message == "":
        final_message = f"Данные по стране: \n" \
                        f"Население: <b>{location[0]['country_population']}</b> \n" \
                        f"Заболевшие: <b>{location[0]['latest']['confirmed']}</b> \n " \
                        f"Умершие: <b>{location[0]['latest']['deaths']}</b> \n"
    bot.send_message(messege.chat.id, final_message, parse_mode='html')


bot.polling(none_stop=True)
all = covid19.getLatest()
Rus = covid19.getLocationByCountryCode("RU")

print(Rus)