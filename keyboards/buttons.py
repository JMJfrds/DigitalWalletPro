from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

balance = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Balance"),KeyboardButton(text="Referral")],
], resize_keyboard=True)
