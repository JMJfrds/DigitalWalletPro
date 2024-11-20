from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from models.user import User

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    user = User(tg_id=message.from_user.id, full_name=message.from_user.full_name, username=message.from_user.username)
    await user.save()
    await message.reply(f"{message.from_user.full_name} welcome back!")
