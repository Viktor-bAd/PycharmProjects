# Користувач вводить висоту трикутника і символ для заповнення.
# Програма повинна вивести трикутник, вирівняний по правому краю.

height = int(input("Введіть висоту: "))
symbol = input("Введіть символ: ")
i = 1
while i <= height:
    print(symbol * i)
    i += 1


# Користувач вводить розміри дошки (ширину і висоту) і два символи для клітинок.
# Програма повинна відобразити шахову дошку, використовуючи ці символи.

width = int(input("Введіть ширину дошки: "))
height = int(input("Введіть висоту дошки: "))
char1 = input("Введіть перший символ: ")
char2 = input("Введіть другий символ: ")
for row in range(height):
    for col in range(width):
        if (row + col) % 2 == 0:
            print(char1, end=" ")
        else:
            print(char2, end=" ")

    print()


# Програма випадковим чином загадує чотиризначне число без цифр,
# що повторюються. Користувач повинен спробувати вгадати це число, вводячи свої варіанти.
# Після кожного введення програма повідомляє:
# Кількість цифр, які стоять на своїх місцях (бики).
# Кількість цифр, які є в числі, але стоять не на своїх місцях (корови).

import random

secret = str(random.randint(1000, 9999))
while True:
    guess = input("\nВведіть 4 цифри: ")
    if guess == secret:
        print("Перемога! 🎉")
        break
    bulls = 0
    cows = 0
    for s, g in zip(secret, guess, strict=False):
        if s == g:
            bulls = bulls + 1
    for char in guess:
        if char in secret:
            cows = cows + 1

    pure_cows = cows - bulls
    print("Бики:", bulls, "Корови:", pure_cows)


# Число Армстронга — це число, яке дорівнює сумі своїх цифр, піднесених до степеня, що дорівнює кількості цифр.
# Напишіть програму, яка:
# Приймає одне число від користувача.
# Перевіряє, чи є воно числом Армстронга.
# Виводить відповідний результат.
number_str = input("Введіть число: ")
count = 0
for char in number_str:
    count = count + 1
total_sum = 0
for char in number_str:
    digit = int(char)
    total_sum = total_sum + (digit**count)
if total_sum == int(number_str):
    print("Це число Армстронга!")
else:
    print("Це не число Армстронга.")


# Користувач вводить висоту ромба (непарне число) і символ для заповнення. Програма повинна вивести заповнений ромб.
# Приклад введення:
# Введіть висоту: 5.
# Введіть символ: #

height = int(input("Введіть висоту: "))
symbol = input("Введіть символ: ")
middle = height // 2
i = 0
while i <= middle:
    spaces = middle - i
    chars = 2 * i + 1
    print(" " * spaces + symbol * chars)
    i += 1
i = middle - 1
while i >= 0:
    spaces = middle - i
    chars = 2 * i + 1
    print(" " * spaces + symbol * chars)
    i -= 1


# Користувач вводить висоту ромба (непарне число) і символ для заповнення. Програма повинна вивести порожнистий ромб.

height = int(input("Введіть висоту: "))
symbol = input("Введіть символ: ")
middle = height // 2
i = 0
while i <= middle:
    space = middle - i
    if i == 0:
        print(" " * space + symbol)
    else:
        spaces_in = 2 * i - 1
        print(" " * space + symbol + " " * spaces_in + symbol)
    i += 1
i = middle - 1
while i >= 0:
    space = middle - i

    if i == 0:
        print(" " * space + symbol)
    else:
        spaces_in = 2 * i - 1
        print(" " * space + symbol + " " * spaces_in + symbol)

    i -= 1
