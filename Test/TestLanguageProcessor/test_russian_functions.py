from LanguageProcessor import russian_functions
import pytest


class TestRussianFunctions:
    @pytest.fixture
    def russian_words(self):
        words = [
            "сказать",
            "банан",
            "жена",
            "спать",
            "саус",
            "шутка",
            "причем",
            "Сталин",
            "Брежнев",
            "Невеста",
        ]

        return words

    @pytest.fixture
    def english_words(self):
        words = [
            "hello",
            "goodbye",
            "discombulate",
            "love",
            "hate",
            "hat",
            "Friends",
            "Porcupine",
            "sArCaSm",
            "Repetition",
        ]

        return words

    def test_check_if_word_is_russian_with_russian_words(self, russian_words):
        results = [
            russian_functions.check_if_word_is_russian(word) for word in russian_words
        ]

        assert all(results)

    def test_check_if_word_is_russian_with_english_words(self, english_words):
        results = [
            russian_functions.check_if_word_is_russian(word) for word in english_words
        ]

        assert not all(results)
