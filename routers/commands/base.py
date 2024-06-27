from aiogram import Router
from aiogram.filters import CommandStart, Command

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start_command(message):
    await message.answer(f'Hello, {message.from_user.full_name}!')


@router.message(Command('help'))
async def handle_help_command(message):
    await message.answer('This is a help message')
