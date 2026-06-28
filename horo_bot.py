import asyncio
import os
from aiohttp import web
import threading
from keyboards.keyboards import get_keyboard
from handlers.callback import router as callback_router
from db import get_all_signs
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import types, F
from aiogram.filters import Command
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    raise ValueError('BOT_TOKEN не найден в .env')
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(callback_router)
@dp.message(Command('start'))
async def start(message: types.Message):
    signs = get_all_signs()
    if not signs:
        await message.answer('Нет данных в базе')
        return
    keyboard = get_keyboard(signs)
    await message.answer('Выберите знак зодиака:', reply_markup=keyboard)
async def handle(request):
    return web.Response(text="Bot is alive")
def run_web():
    app = web.Application()
    app.router.add_get("/", handle)
    web.run_app(app, port=8080)
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    threading.Thread(target=run_web, daemon=True).start()
    asyncio.run(main())