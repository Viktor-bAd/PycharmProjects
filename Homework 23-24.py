# Завдання 1
# Користувач з клавіатури вводить список цілих чисел. Необхідно порахувати, скільки у списку парних і непарних чисел.
# Результати вивести на екран.

numbers = input("Введіть числа через пробіл: ").split()
numbers = [int(x) for x in numbers]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Парних чисел:", even_count)
print("Непарних чисел:", odd_count)

# Завдання 2
# Користувач із клавіатури вводить список цілих чисел. Необхідно визначити максимальне і мінімальне значення у списку.
# Результати вивести на екран.

numbers = [int(x) for x in input("Введіть числа через пробіл: ").split()]
min_value = numbers[0]
max_value = numbers[0]
for num in numbers:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

print("Мінімальне значення:", min_value)
print("Максимальне значення:", max_value)

# У списку цілих, заповненому випадковими числами, визначити мінімальний, додатний елемент і максимальний,
# від'ємний елемент, порахувати кількість від'ємних елементів, порахувати кількість додатних елементів,
# порахувати кількість нулів. Результати вивести на екран.

import random
n = int(input("Введіть кількість елементів списку: "))
numbers = [random.randint(-50, 50) for _ in range(n)]
print("Список:", numbers)
min_positive = None
max_negative = None
count_positive = 0
count_negative = 0
count_zero = 0

for num in numbers:
    if num > 0:
        count_positive += 1
        if min_positive is None or num < min_positive:
            min_positive = num
    elif num < 0:
        count_negative += 1
        if max_negative is None or num > max_negative:
            max_negative = num
    else:
        count_zero += 1

print("Мінімальний додатній елемент:", min_positive)
print("Максимальний від'ємний елемент:", max_negative)
print("Кількість додатних елементів:", count_positive)
print("Кількість від'ємних елементів:", count_negative)
print("Кількість нулів:", count_zero)

# Користувач із клавіатури вводить список цілих чисел і деяке число.
# Необхідно видалити зі списку всі елементи, які менші за задане число. Результат вивести на екран.

numbers = [int(x) for x in input("Введіть числа через пробіл: ").split()]
limit = int(input("Введіть число-поріг: "))
result = [num for num in numbers if num >= limit]
print("Результат:", result)

# Користувач вводить з клавіатури арифметичний вираз. Наприклад, 23+12.
# Необхідно вивести на екран результат виразу. У нашому прикладі це 35.
# Арифметичний вираз може складатися тільки з трьох частин: число, операція, число. Можливі операції: +, -, *, /.

expr = input("Введіть арифметичний вираз (наприклад 23+12): ")
if '+' in expr:
    num1, num2 = expr.split('+')
    result = int(num1) + int(num2)
elif '-' in expr:
    num1, num2 = expr.split('-')
    result = int(num1) - int(num2)
elif '*' in expr:
    num1, num2 = expr.split('*')
    result = int(num1) * int(num2)
elif '/' in expr:
    num1, num2 = expr.split('/')
    result = int(num1) / int(num2)
else:
    result = None
    print("Невідомий оператор")
if result is not None:
    print("Результат:", result)


# Користувач із клавіатури вводить список цілих чисел. Необхідно відсортувати цей список так,
# щоб від('ємні числа залишилися на своїх місцях, а решта елементів були відсортовані за зростанням. '
# Результат вивести на екран.)

numbers = [int(x) for x in input("Введіть числа через пробіл: ").split()]
positives = [num for num in numbers if num >= 0]
positives.sort()
index = 0
result = []
for num in numbers:
    if num < 0:
        result.append(num)
    else:
        result.append(positives[index])
        index += 1

print("Відсортований список:", result)