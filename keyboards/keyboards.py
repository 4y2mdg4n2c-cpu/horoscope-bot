from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
def get_keyboard(signs):
    keyboard = [
        [InlineKeyboardButton(text=sign.capitalize(), callback_data=sign)]
        for sign in signs()
    ]
    keyboard.append([InlineKeyboardButton(text="🔄 Обновить", callback_data="update")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)