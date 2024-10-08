import json
from pathlib import Path
from bot import settings


def load_translations():
    translations_file = Path(__file__).parent.parent / "locales" / "translations.json"
    with open(translations_file, "r", encoding="utf-8") as file:
        return json.load(file)


translations = load_translations()


def get_translation(key, lang=None, **kwargs):
    lang = lang or settings.BOT_LANGUAGE or "en"
    try:
        message = translations[lang][key]
        return message.format(**kwargs)
    except KeyError:
        return f"Translation not found for key: {key}"
