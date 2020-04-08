from covid import Covid
import telebot
from telebot import types
covid = Covid(source="worldometers")
covid.get_data()
bot = telebot.TeleBot("1226498564:AAEFV3lY3XXSDIDtpdSrO1FiMtUYbCc7ZKE")

@bot.message_handler(commands=['start'])
def start(message):
    send_message = f"<b>Привет, {message.from_user.first_name}!</b>\n Если тебя интересует актуальная информация о коронавирусе," \
                   f"\n я могу тебе помочь. Просто напиши интересующую тебя страну\n\n"
    bot.send_message(message.chat.id, send_message, parse_mode='html',reply_markup=keyboard())
@bot.message_handler(content_types=['text'])
def send_text(message):
	final_message=""
	get_message_bot = message.text.strip().lower()
	if get_message_bot =='украина':
		location = covid.get_status_by_country_name("ukraine")
	elif get_message_bot =='россия':
		location = covid.get_status_by_country_name("russia")
	elif get_message_bot =='беларусь':
		location = covid.get_status_by_country_name("belarus")
	elif get_message_bot =='сша':
		location = covid.get_status_by_country_name("usa")
	elif get_message_bot =='италия':
		location = covid.get_status_by_country_name("italy")
	elif get_message_bot =='германия':
		location = covid.get_status_by_country_name("germany")
	elif get_message_bot =='франция':
		location = covid.get_status_by_country_name("france")
	elif get_message_bot =='китай':
		location = covid.get_status_by_country_name("china")
	elif get_message_bot =='мир🌍':
		final_message=2
	else:
		if message.chat.id ==267418139:
			final_message = f"Не знаю таких стран,но держи цём от Назара😚"
		else:
			final_message = f"Нет информации о данной стране или ее не существет"




	if final_message =="":
		final_message = f"Сводка\n<b>Болеющих сейчас: </b>{location['active']:,}\n<b>Заболевших сегодня: </b>{location['new_cases']:,}\n"\
						f"<b>Умерших сегодня: </b>{location['new_deaths']:,}\n<b>Выздоровевшие: </b>{location['recovered']:,}\n" \
						f"<b>Сметрей за все время: </b>{location['deaths']:,}\n<b>Больных за все время: </b>{location['confirmed']:,}"
	elif final_message ==2:
		final_message = f"<b>Больных за все время: </b> {covid.get_total_active_cases()}\n" \
						f"<b>Сейчас болеют: </b> {covid.get_total_confirmed_cases()}\n" \
						f"<b>Выздоровевшие: </b> {covid.get_total_recovered()}\n" \
						f"<b>Сметрей: </b> {covid.get_total_deaths()}\n"

	bot.send_message(message.chat.id, final_message,parse_mode='html', reply_markup=keyboard())



def keyboard():
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton('Мир🌍')
	btn2 = types.KeyboardButton('Украина')
	btn3 = types.KeyboardButton('Россия')
	btn4 = types.KeyboardButton('Беларусь')
	markup.add(btn1, btn2, btn3, btn4)
	return markup



bot.polling(none_stop=True)

