from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.inline_keyboards import begin_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n\n"
                         f"Что умеет этот бот? \n"
                         f"Остался один шаг для завершения регистрации на бесплатный вебинар\n\n"
                         f" 'Как с помощью ТАРО прийти к балансу во всех сферах' – нажмите кнопку 'начать'",
                         reply_markup=begin_keyboard)
