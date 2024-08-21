from cou.constants import EXTENSIONS


def get_language_by_extension(extension) -> str:
    for language, extensions in EXTENSIONS.items():
        if extension in extensions:
            return language


def format_number(num: int) -> str:
    return f"{num:,}".replace(',', '.')


def get_max_language_len(languages: dict) -> int:
    max_lang_len = max(len(lang) for lang in languages.keys())
    max_lines_len = max(len(format_number(lines)) for lines in languages.values())

    return max_lang_len + max_lines_len
