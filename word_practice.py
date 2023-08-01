# %%
import spacy
from spacy.tokenizer import Tokenizer
from collections import Counter
from spacy.lang.fr.stop_words import STOP_WORDS as french_stop_words

# %%
nlp = spacy.load("ru_core_news_sm")
nlp.Defaults.stop_words = french_stop_words

doc = nlp("здраствуйте товарищ. Это - предложение. Я тебя люблю!")
# %%

for word in doc:
    print(word.text, word.lemma_)
# %%

with open("data/RU/Tolstoy/WarAndPeace/Chapter1.txt", "r") as file:
    lines = file.readlines()

    text = " ".join([line.strip() for line in lines])

    doc = nlp(text)
# %%
for word in doc:
    print(f"{word.text},\t{word.lemma},\t{word.lemma_}\t{word.is_alpha}")
# %%

word_counter = Counter()

for word in doc:
    if not word.is_stop and word.is_alpha:
        # if word.is_alpha:
        word_counter.update({word.lemma_: 1})
# %%

russian_letters = [
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
]


def check_if_text_is_russian(txt_to_check):
    return all([c in russian_letters for c in txt_to_check])


russian_word_counter = Counter()

for word in doc:
    if not word.is_stop and word.is_alpha and check_if_text_is_russian(word.lemma_):
        # if word.is_alpha:
        russian_word_counter.update({word.lemma_: 1})
# %%
