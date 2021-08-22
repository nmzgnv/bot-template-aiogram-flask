from aiogram import Bot, Dispatcher, types

from bot.states.SQLAlchemyStorage import SQLAlchemyStorage
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = SQLAlchemyStorage()
dp = Dispatcher(bot, storage=storage)
