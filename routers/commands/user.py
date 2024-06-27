from aiogram import Router
from aiogram.filters import Command

router = Router(name=__name__)


@router.message(Command('download'))
async def handle_help_command(message):
    await message.answer('To download a file, send me a url!')
