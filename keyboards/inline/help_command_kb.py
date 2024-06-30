from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core.constants import PROJECT_URL
from utils.locales import get_locale_text


def build_help_command_kb(locale: str = 'ru') -> InlineKeyboardMarkup:
    bot_source_code_btn = InlineKeyboardButton(
        text=get_locale_text('BOT_SOURCE_CODE_BTN_TEXT', locale),
        url=PROJECT_URL,
    )
    return InlineKeyboardMarkup(inline_keyboard=[[bot_source_code_btn]])
