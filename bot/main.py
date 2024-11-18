import asyncio
from aiogram import Bot, Dispatcher
from bot.config import BOT_TOKEN
from bot.handlers import register_all_handlers


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    register_all_handlers(dp)
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())
