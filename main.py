import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


async def main():
    load_dotenv()
    dp = Dispatcher()
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
