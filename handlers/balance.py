from aiogram import Router, F
from services.user import get_user
from aiogram.types import Message

router = Router()

coin = "https://unsplash.com/photos/a-pile-of-coins-sitting-on-top-of-a-table-tqdFbTeVlk8"


@router.message(F.text == 'Balance')
async def cdm_balance(message: Message):
    user = await get_user(message.from_user.id)
    if user:
        await message.answer_photo(photo=f"{coin}", caption=f"Balansingiz:\n🌕{user.balance}")
    else:
        await message.answer("balance not found")
