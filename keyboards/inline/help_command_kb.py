from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build_help_command_kb() -> InlineKeyboardMarkup:
    bot_source_code_btn = InlineKeyboardButton(
        text='🤖 Исходный код бота',
        url='https://github.com/vernette/web2gram'
    )
    return InlineKeyboardMarkup(inline_keyboard=[[bot_source_code_btn]])
