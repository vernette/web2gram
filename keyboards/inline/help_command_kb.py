from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.locales import load_locales

locales = load_locales()


def build_help_command_kb(locale: str = 'ru') -> InlineKeyboardMarkup:
    bot_source_code_btn = InlineKeyboardButton(
        text=locales[locale]['BOT_SOURCE_CODE_BTN_TEXT'],
        url='https://github.com/vernette/web2gram',
    )
    return InlineKeyboardMarkup(inline_keyboard=[[bot_source_code_btn]])
