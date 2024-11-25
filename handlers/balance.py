from aiogram import Router, F
from services.user import get_balance
from aiogram.types import Message

router = Router()


@router.message(F.text == 'Balance')
async def cmd_balance(message: Message):
    balance = get_balance(message.from_user.id)
    if balance:
        await message.answer(f"{message.from_user.full_name} is {balance} 🌕")
    else:
        await message.answer(f'{message.from_user.full_name} has not balance')
