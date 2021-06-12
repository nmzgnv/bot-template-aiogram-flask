from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from bot.loader import dp
from database.models import User
from bot.texts import _


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    referer_id = ''
    command_args = message.text.split('start ')
    if len(command_args) > 1:
        referer_id = command_args[1]
    User.register(message.from_user, referer_id=referer_id)

    await message.answer(_('start_text').format(message.from_user.full_name))
