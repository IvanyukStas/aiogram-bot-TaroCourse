from aiogram import types

begin_button = types.InlineKeyboardButton('Начать', callback_data='begin')
begin_keyboard = types.InlineKeyboardMarkup(row_width=1)
begin_keyboard.insert(begin_button)


