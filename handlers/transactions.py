from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from services.user import check_address
from utils.states import SendCoins

router = Router()


@router.message(F.text == "Send Coin")
async def send_coins(message: Message, state: FSMContext):
    await message.answer("Referral Address:")
    await state.set_state(SendCoins.token)


@router.message(SendCoins.token)
async def get_address(message: Message, state: FSMContext):
    token = message.text
    addr = await check_address(token)
    if addr:
        await state.update_data(address=token)
        await message.answer("Enter the amount to send:")
        await state.set_state(SendCoins.amount)
    else:
        await message.answer("Noto‘g‘ri referral address. Qayta kiriting.") # noqa

