import asyncio
import os
from horo import get_horoscope_data
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    raise ValueError('BOT_TOKEN не найден в .env')
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
def get_keyboard(data):
    keyboard = [
        [InlineKeyboardButton(text=sign.capitalize(), callback_data=sign)]
        for sign in data.keys()
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)
@dp.message(Command('start'))
async def start(message: types.Message):
    data = get_horoscope_data()
    if not data:
        await message.answer('Ошибка получения данных')
        return
    keyboard = get_keyboard(data)
    await message.answer('Выберите знак зодиака:', reply_markup=keyboard)
@dp.callback_query()
async def get_sign(call: types.CallbackQuery):
    sign = call.data
    data = get_horoscope_data()
    forecast = data.get(sign)
    if forecast:
        await call.message.answer(forecast)
    else:
        await call.message.answer("Не найден прогноз")
    await call.answer()
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())