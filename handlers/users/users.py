import logging

from aiogram import types

from loader import dp, bot


@dp.callback_query_handler(text='begin')
async def begin(call: types.CallbackQuery):
    await call.message.answer(f'Ура!  Вы успешно зарегистрировались на вебинар Ирэны и Юли "Как с помощью ТАРО прийти'
                              f' к балансу во всех сферах!".', reply_markup=types.ReplyKeyboardRemove())
    await call.message.edit_reply_markup()


@dp.channel_post_handler()
async def channel_repost(post: types.Message):
    logging.info(f'Делаем репост')
    await bot.send_message('193293589', f'{post.text}')