from aiogram import executor
from config import settings
from handlers import dp

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
