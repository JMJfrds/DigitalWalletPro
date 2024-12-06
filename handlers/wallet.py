from aiogram import Router, F
from aiogram.types import Message

from services.user import get_user

router = Router()

img_wallet = "https://unsplash.com/photos/wallet-credit-card-and-gold-coins-isolated-on-blue-background-money-saving-concept-3d-rendering-with-clipping-path-0OxGmiF6SZU"


@router.message(F.text == "Wallet")
async def wallets(message: Message):
    referral = await get_user(message.from_user.id)
    msg_text = f"""
💳 Sizning Walletingiz! 💳

Balansingiz:\n🌕 {referral.balance}
Wallet manzilingiz:📤\n<code>{referral.referral_code}</code>

    """
    await message.answer_photo(img_wallet, caption=msg_text,parse_mode='HTML')
