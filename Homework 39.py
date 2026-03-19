

# Завдання 1

# Lambda-функція, що множить число на -1
multiply_by_minus_one = lambda x: -x
"""
Повертає число, помножене на -1.

:param x: число (int або float)
:return: число з протилежним знаком
"""


# Lambda-функція, що перевіряє, чи рядок непорожній
is_non_empty_string = lambda s: s != ""
"""
Перевіряє, чи є рядок непорожнім.

:param s: рядок
:return: True, якщо рядок не порожній, інакше False
"""

print(multiply_by_minus_one(10))   # -10
print(is_non_empty_string("Hi"))   # True
print(is_non_empty_string(""))     # False


#Завдання 2

nums = [1, 2, 3, 4, 5]

def filter_above_average(numbers: list[float]) -> list[float]:
    """
    Повертає список чисел, які більші за середнє арифметичне.

    :param numbers: список чисел
    :return: список чисел, більших за середнє значення
    """
    if not numbers:
        return []

    average = sum(numbers) / len(numbers)
    return list(filter(lambda x: x > average, numbers))

print(filter_above_average(nums))


words = ["tree", "sun", "moon", "star", "sky"]

def filter_words_with_four_letters(words: list[str]) -> list[str]:
    """
    Повертає список слів, у яких рівно 4 літери.

    :param words: список слів
    :return: список слів довжиною 4 символи
    """
    return list(filter(lambda word: len(word) == 4, words))

print(filter_words_with_four_letters(words))


# Завдання 3

words = ["banana", "apple", "avocado", "grape"]

def find_word_with_most_letter(letter: str, words: list[str]) -> str:
    """
    Повертає слово зі списку, в якому найбільша кількість заданої літери.

    :param letter: літера для пошуку
    :param words: список слів
    :return: слово з найбільшою кількістю цієї літери
    """
    if not words:
        return ""

    normalized_letter = letter.lower()

    return max(
        words,
        key=lambda word: word.lower().count(normalized_letter)
    )

print(find_word_with_most_letter(letter="a", words=words))

