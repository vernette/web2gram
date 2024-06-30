import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from routers import router as main_router
from utils.base import setup_logging


async def main():
    load_dotenv()
    dp = Dispatcher()
    dp.include_router(main_router)
    bot = Bot(
        os.getenv('BOT_TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    setup_logging()
    asyncio.run(main())
