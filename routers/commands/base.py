from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.help_command_kb import build_help_command_kb
from keyboards.inline.language_selector_kb import build_language_selector_kb
from utils.locales import load_locales

router = Router(name=__name__)


locales = load_locales()
user_languages = dict()  # TODO Replace with DB


@router.message(CommandStart())
async def handle_start_command(message: Message):
    user_language_code = message.from_user.language_code
    message_text = locales[user_language_code]['CHOOSE_LANGUAGE_MESSAGE']
    await message.answer(text=message_text, reply_markup=build_language_selector_kb())


@router.callback_query(F.data.startswith('lang_'))
async def handle_language_choice(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    chosen_lang = callback_query.data.split('_')[1]
    user_languages[user_id] = chosen_lang
    await callback_query.answer()
    await callback_query.message.answer(
        locales[chosen_lang]['START_COMMAND_MESSAGE'].format(
            full_name=callback_query.from_user.full_name
        ),
        parse_mode=ParseMode.HTML,
    )


@router.message(Command('help'))
async def handle_help_command(message: Message):
    bot_info = await message.bot.me()
    user_language = user_languages.get(message.from_user.id, 'ru')
    help_message = locales[user_language]['HELP_COMMAND_MESSAGE'].format(
        bot_username=bot_info.username
    )
    await message.answer(
        text=help_message,
        disable_web_page_preview=True,
        reply_markup=build_help_command_kb(locale=user_language),
        parse_mode=ParseMode.HTML,
    )
