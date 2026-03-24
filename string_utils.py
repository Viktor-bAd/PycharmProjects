"""
Модуль string_utils.py

Функції для роботи з рядками:
- видалення знаків пунктуації
- підрахунок голосних
- перевірка на паліндром
"""


def remove_punctuation(text: str) -> str:
    """
    Видаляє з рядка знаки пунктуації: , . ? ! ; :

    :param text: str - Вхідний рядок
    :return: str - Рядок без зазначених знаків пунктуації
    """
    punctuation = ",.?!;:"

    # Створюємо таблицю для видалення символів
    translation_table = str.maketrans("", "", punctuation)

    return text.translate(translation_table)


def count_vowels(text: str) -> int:
    """
    Підраховує кількість голосних літер у рядку.
    Регістр не враховується.

    :param text: str - Вхідний рядок
    :return: int - Кількість голосних
    """
    vowels = "aeiouyаеєиіїоуюя"

    text = text.lower()

    # Використовуємо метод count()
    return sum(text.count(vowel) for vowel in vowels)


def is_palindrome(text: str) -> bool:
    """
    Перевіряє, чи є рядок паліндромом.
    Ігнорує регістр, пробіли та знаки пунктуації.

    :param text: str - Вхідний рядок
    :return: bool
    """
    # Видаляємо пунктуацію
    cleaned = remove_punctuation(text)

    # Прибираємо пробіли і приводимо до нижнього регістру
    cleaned = cleaned.replace(" ", "").lower()

    # Перевірка через зріз
    return cleaned == cleaned[::-1]
