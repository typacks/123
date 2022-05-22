from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def admin_menu():
	button1 = KeyboardButton('Статистика')
	button2 = KeyboardButton('Рассылка')
	button3 = KeyboardButton('Назад')
	admin1_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	admin1_kb.add(button1)
	admin1_kb.add(button2)
	admin1_kb.add(button3)
	return admin1_kb
def back_2():
	back_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	button = KeyboardButton('Отмена')
	back_kb1.add(button)
	return back_kb1
def admin_start():
	back_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	button = KeyboardButton('Админка')
	back_kb1.add(button)
	return back_kb1
