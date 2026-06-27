from aiogram import Router, F
from aiogram.types import CallbackQuery
from services.horoscope import get_sign_forecast
from db import get_forecast
from update_db import update_db

router = Router()


@router.callback_query(F.data == "update")
async def update_handler(call: CallbackQuery):
    await call.message.answer("Обновляю базу...")

    update_db()

    await call.message.answer("База обновлена ✅")
    await call.answer()


@router.callback_query()
async def sign_handler(call: CallbackQuery):
    sign = call.data

    forecast = get_sign_forecast(sign)

    if forecast:
        await call.message.answer(forecast)
    else:
        await call.message.answer("Не найден прогноз")

    await call.answer()