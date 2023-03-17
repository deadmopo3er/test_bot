from aiogram import types
from config import settings

@settings.dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.reply("Welcome to the Event Coordinator bot!")
