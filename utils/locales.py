import json
import os


locales_folder = os.path.join(os.path.dirname(__file__), '../core/locales')


def load_locales():
    locales = {}
    for filename in os.listdir(locales_folder):
        if filename.endswith('.json'):
            lang = filename.split('.')[0]
            with open(
                os.path.join(locales_folder, filename), 'r', encoding='utf-8'
            ) as file:
                locales[lang] = json.load(file)
    return locales


def get_locale_text(key: str, locale: str = 'ru'):
    locales = load_locales()
    return locales[locale][key]
