from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from core.constants import START_COMMAND_MESSAGE, HELP_COMMAND_MESSAGE

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start_command(message: Message):
    await message.answer(
        START_COMMAND_MESSAGE.format(full_name=message.from_user.full_name)
    )


@router.message(Command('help'))
async def handle_help_command(message: Message):
    bot_info = await message.bot.me()
    await message.answer(
        text=HELP_COMMAND_MESSAGE.format(bot_username=bot_info.username),
        disable_web_page_preview=True,
    )
