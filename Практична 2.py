# 1 Підносить число до квадрату
square = lambda x: x ** 2

# 2 Повертає периметр трикутника за сторонами a, b, c
perimeter = lambda a, b, c: a + b + c

# 3 Форматує "Прізвище, Ім’я"
format_name = lambda first_name, last_name: f"{last_name}, {first_name}"

# 4 Перевіряє, чи є число парним (повертає True/False)
is_even = lambda x: x % 2 == 0


print(square(5))                   # 25
print(perimeter(3, 4, 5)) # 12
print(format_name("Віктор", "Бодашко"))
print(is_even(8))                   # True
print(is_even(7))                   # False



from typing import List


def get_positive_numbers(numbers: List[float]) -> List[float]:
    """
    Повертає список лише додатніх чисел, використовуючи filter().

    :param numbers: List[float] - вхідний список чисел (можуть бути додатні, від'ємні, нуль)
    :return: List[float] - новий список, що містить тільки числа > 0
    """
    return list(filter(lambda x: x > 0, numbers))

nums = [-5, 0, 3.2, 7, -1]
print(get_positive_numbers(nums))  # Виведе: [3.2, 7]


def filter_long_words(words: List[str]) -> List[str]:
    """
    Повертає список слів, у яких більше ніж 3 літери, використовуючи filter().

    :param words: List[str] - вхідний список слів
    :return: List[str] - новий список, що містить слова з довжиною > 3 символи
    """
    return list(filter(lambda word: len(word) > 3, words))

words = ["cat", "house", "sun", "tree", "a"]
print(filter_long_words(words))  # Виведе: ['house', 'tree']


def filter_words_by_letter(words: List[str], letter: str) -> List[str]:
    """
    Повертає список слів, які починаються на вказану літеру (регістр неважливий),
    використовуючи filter().

    :param words: List[str] - вхідний список слів
    :param letter: str - літера, з якої мають починатися слова (один символ)
    :return: List[str] - список слів, що починаються на задану літеру (без урахування регістру)
    """
    normalized_letter = letter.lower()
    return list(filter(lambda word: word.lower().startswith(normalized_letter), words))

words = ["Apple", "apricot", "banana", "Avocado", "berry"]
print(filter_words_by_letter(words, "a"))  # Виведе: ['Apple', 'apricot', 'Avocado']


import time
from typing import Callable, Any


def measure_execution_time(func: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
    """
    Вимірює час виконання переданої функції в секундах.

    :param func: Callable[..., Any] - функція, час виконання якої потрібно виміряти
    :param args: Any - позиційні аргументи, які будуть передані у func
    :param kwargs: Any - іменовані аргументи, які будуть передані у func
    :return: float - час виконання функції у секундах
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time


# Приклад використання (для тесту):

def example_function(n: int) -> int:
    """
    Приклад функції, для якої ми будемо вимірювати час виконання.
    Наприклад, проста сума чисел від 0 до n.

    :param n: int - межа сумування
    :return: int - сума чисел від 0 до n
    """
    total = 0
    for i in range(n + 1):
        total += i
    return total

execution_time = measure_execution_time(example_function, 2)
print(f"Час виконання: {execution_time:.3f} секунд")



def sort_by_last_letter(words: List[str]) -> List[str]:
    """
    Сортує список слів за останньою літерою.

    :param words: List[str] - список слів
    :return: List[str] - відсортований список слів
    """
    return sorted(words, key=lambda word: word[-1])

words = ["apple", "banana", "cherry", "date"]
print(sort_by_last_letter(words))


def sort_numbers_by_digit_count(numbers: List[int]) -> List[int]:
    """
    Сортує список чисел за кількістю цифр.

    :param numbers: List[int] - список цілих чисел
    :return: List[int] - список, відсортований за довжиною числа
    """
    return sorted(numbers, key=lambda num: len(str(abs(num))))

numbers = [1, 23, 456, -7, 89, -1234]
print(sort_numbers_by_digit_count(numbers))


def find_closest_number(numbers: List[float], target: float) -> float:
    """
    Повертає число зі списку, яке найближче до заданого.

    :param numbers: List[float] - список чисел
    :param target: float - число, до якого шукається найменша різниця
    :return: float - найближче число
    """
    return min(numbers, key=lambda num: abs(num - target))

numbers = [10.5, 3.2, 7.8, 4.4]
target = 5
print(find_closest_number(numbers, target))


def find_shortest_word(words: List[str]) -> str:
    """
    Повертає слово з найменшою довжиною зі списку.

    :param words: List[str] - список слів
    :return: str - найкоротше слово
    """
    return min(words, key=len)

words = ["apple", "to", "banana", "a", "pear"]
print(find_shortest_word(words))


def sort_numbers_by_digits_then_value(numbers: List[int]) -> List[int]:
    """
    Сортує числа спочатку за кількістю цифр, а при рівній кількості — за значенням.

    :param numbers: List[int] - список цілих чисел
    :return: List[int] - відсортований список
    """
    return sorted(numbers, key=lambda num: (len(str(abs(num))), num))

numbers = [1, 23, 4, 456, -12, 89, -7]
print(sort_numbers_by_digits_then_value(numbers))


