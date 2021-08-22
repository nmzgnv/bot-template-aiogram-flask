from aiogram import Bot, Dispatcher, types
# from database.SQLAlchemyStorage import SQLAlchemyStorage
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# storage = SQLAlchemyStorage()
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
