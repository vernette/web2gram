from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.help_command_kb import build_help_command_kb
from keyboards.inline.language_selector_kb import build_language_selector_kb
from utils.locales import get_locale_text

router = Router(name=__name__)

user_languages = dict()  # TODO Replace with DB


@router.message(CommandStart())
async def handle_start_command(message: Message):
    await message.answer(
        text=get_locale_text(
            'CHOOSE_LANGUAGE_MESSAGE', message.from_user.language_code
        ),
        reply_markup=build_language_selector_kb(),
    )


@router.callback_query(F.data.startswith('lang_'))
async def handle_language_choice(callback_query: CallbackQuery):
    chosen_lang = callback_query.data.split('_')[1]
    user_languages[callback_query.from_user.id] = chosen_lang
    await callback_query.answer()
    await callback_query.message.delete()
    await callback_query.message.answer(
        get_locale_text('START_COMMAND_MESSAGE', chosen_lang).format(
            full_name=callback_query.from_user.full_name
        )
    )


@router.message(Command('help'))
async def handle_help_command(message: Message):
    bot_info = await message.bot.me()
    user_language = user_languages.get(message.from_user.id, 'ru')
    help_message = get_locale_text('HELP_COMMAND_MESSAGE', user_language).format(
        bot_username=bot_info.username
    )
    await message.answer(
        text=help_message,
        disable_web_page_preview=True,
        reply_markup=build_help_command_kb(locale=user_language),
    )
