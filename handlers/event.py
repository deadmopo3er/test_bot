from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ParseMode
from aiogram.utils.markdown import text

from config import settings
from models.event import Event
from services.event_service import create_event, edit_event, delete_event
from utils.keyboard import event_keyboard

class EventStates:
    NEW = "new_event"
    EDIT = "edit_event"
    DELETE = "delete_event"

@settings.dp.message_handler(Command("create_event"), state=None)
async def cmd_create_event(message: types.Message):
    await message.reply("Enter the event details in the following format:\nTitle;Date;Time;Location;Description")
    await EventStates.NEW.set()

@settings.dp.message_handler(lambda message: message.text, state=EventStates.NEW)
async def process_new_event(message: types.Message, state: FSMContext):
    event_data = message.text.split(";")
    if len(event_data) != 5:
        await message.reply("Invalid format, please try again.")
        return

    title, date, time, location, description = event_data
    new_event = create_event(title, date, time, location, description)
    if new_event:
        response = text(f"Event '{new_event.title}' created successfully!")
    else:
        response = "Error creating the event. Please try again."

    await message.reply(response)
    await state.finish()

@settings.dp.message_handler(Command("edit_event"), state=None)
async def cmd_edit_event(message: types.Message):
    await message.reply("Enter the event ID followed by the updated event details in the following format:\nID;Title;Date;Time;Location;Description")
    await EventStates.EDIT.set()

@settings.dp.message_handler(lambda message: message.text, state=EventStates.EDIT)
async def process_edit_event(message: types.Message, state: FSMContext):
    event_data = message.text.split(";")
    if len(event_data) != 6:
        await message.reply("Invalid format, please try again.")
        return

    event_id, title, date, time, location, description = event_data
    edited_event = edit_event(event_id, title, date, time, location, description)
    if edited_event:
        response = text(f"Event '{edited_event.title}' updated successfully!")
    else:
        response = "Error updating the event. Please try again."

    await message.reply(response)
    await state.finish()

@settings.dp.message_handler(Command("delete_event"), state=None)
async def cmd_delete_event(message: types.Message):
    await message.reply("Enter the event ID you want to delete:")
    await EventStates.DELETE.set()

@settings.dp.message_handler(lambda message: message.text, state=EventStates.DELETE)
async def process_delete_event(message: types.Message, state: FSMContext):
    event_id = message.text
    deleted_event = delete_event(event_id)
    if deleted_event:
        response = text(f"Event '{deleted_event.title}' deleted successfully!")
    else:
        response = "Error deleting the event. Please try again."

    await message.reply(response)
    await state.finish()

