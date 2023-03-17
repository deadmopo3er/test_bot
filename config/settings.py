from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand
from aiogram.utils import executor
from aiogram.utils.markdown import text, quote_html
from aiogram import Bot

API_TOKEN = "5228697828:AAHmT4rxELBFZecaERQxo6IxUMCAnZnBYUc"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
