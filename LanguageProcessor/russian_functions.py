RUSSIAN_LETTERS = [
    "й",
    "ц",
    "у",
    "к",
    "е",
    "н",
    "г",
    "ш",
    "щ",
    "з",
    "х",
    "ъ",
    "ф",
    "ы",
    "в",
    "а",
    "п",
    "р",
    "о",
    "л",
    "д",
    "ж",
    "э",
    "я",
    "ч",
    "с",
    "м",
    "и",
    "т",
    "ь",
    "б",
    "ю",
    "Й",
    "Ц",
    "У",
    "К",
    "Е",
    "Н",
    "Г",
    "Ш",
    "Щ",
    "З",
    "Х",
    "Ъ",
    "Ф",
    "Ы",
    "В",
    "А",
    "П",
    "Р",
    "О",
    "Л",
    "Д",
    "Ж",
    "Э",
    "Я",
    "Ч",
    "С",
    "М",
    "И",
    "Т",
    "Ь",
    "Б",
    "Ю",
    "ё",
    "Ё",
]


def check_if_word_is_russian(word_to_check: str) -> bool:
    """
    Checks if a word is a Russian word by making sure all letters in the word belong to
    the Cyrillic alphabet.

    Parameters
    ----------
    word_to_check : str
        The word to check.

    Returns
    -------
    bool
        True if the word is Russian, False if not.
    """
    word_to_check = word_to_check.strip()
    return all([letter in RUSSIAN_LETTERS for letter in word_to_check])
