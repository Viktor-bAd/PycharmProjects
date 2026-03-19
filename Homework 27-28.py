# Завдання 1:

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)

num = int(input("Введіть число: "))
print("Сума цифр:", sum_digits(num))


# Завдання 2:

def is_symmetric(lst, l, r):

    if l >= r:
        return True

    if lst[l] != lst[r]:
        return False

    return is_symmetric(lst, l + 1, r - 1)


nums = list(map(int, input("Введи числа через пробіл: ").split()))

if is_symmetric(nums, 0, len(nums) - 1):
    print("Список симетричний")
else:
    print("Список не симетричний")

# Завдання 3

import random

def count_bulls_cows(secret, guess):
    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def play(secret, attempts=0):
    guess = input("Введи 4-цифрове число: ")

    if len(guess) != 4 or not guess.isdigit():
        print("Будь ласка 4 цифри!")
        return play(secret, attempts)

    attempts += 1

    bulls, cows = count_bulls_cows(secret, guess)
    print(f"Бики: {bulls}, Корови: {cows}")

    if bulls == 4:
        print(f"Вітаю! Ти вгадав число {secret} за {attempts} спроб.")
        return
    else:
        play(secret, attempts)

secret_number = "".join([str(random.randint(0, 9)) for _ in range(4)])

play(secret_number)