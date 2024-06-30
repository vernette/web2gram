from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core.constants import RUSSIAN_LANGUAGE_BTN_TEXT, ENGLISH_LANGUAGE_BTN_TEXT


def build_language_selector_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=RUSSIAN_LANGUAGE_BTN_TEXT,
                    callback_data='lang_ru'
                ),
                InlineKeyboardButton(
                    text=ENGLISH_LANGUAGE_BTN_TEXT,
                    callback_data='lang_en'
                ),
            ]
        ]
    )
