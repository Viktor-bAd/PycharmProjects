# Напишіть функцію, яка відображає на екран форматований текст, зазначений нижче:

def quote():
    lines = [
        "Don't compare yourself with anyone in this world…",
        "if you do so, you are insulting yourself.",
        "Bill Gates"
    ]

    space = 0
    for line in lines:
        print(" " * space + line)
        space += 1

quote()

# Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними.

def print_num(a, b):
    start = min(a, b)
    end = max(a, b)

    for num in range(start, end + 1):
        if num % 2 == 0:
            print(num, end=" ")



print_num(3, 12)


# Напишіть функцію, яка відображає порожній або заповнений квадрат з деякого символу.
# Функція приймає як параметри: довжину сторони квадрата, символ і змінну логічного типу:
# якщо вона дорівнює True, квадрат заповнений;
# якщо False, квадрат порожній.

def draw_square(n, c, f):
    for i in range(n):
        if f:
            print(c * n)
        else:
            if i == 0 or i == n - 1:
                print(c * n)
            else:
                print(c + " " * (n - 2) + c)

draw_square(5, "*", True)
print()
draw_square(5, "#", False)

# Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри

def min_five(a, b, c, d, e):
    return min(a, b, c, d, e)

print(min_five(10, 3, 7, 5, 8))

# Напишіть функцію, яка рахує кількість цифр у числі. Число передається як параметр.
# З функції потрібно повернути отриману кількість цифр. Наприклад, якщо передали 3456, кількість цифр буде 4.
def count_digits(n):
    return len(str(n))
print(count_digits(3213))

# Напишіть функцію, яка перевіряє чи є число паліндромом. Число передається як параметр.
# Якщо число паліндром, потрібно повернути з функції true, інакше false.

def is_palindrome(n):
    n_str = str(n)
    length = len(n_str)
    half = length // 2
    first_half = n_str[:half]
    second_half = n_str[-half:][::-1]
    return first_half == second_half

print(is_palindrome(123321))  # True
print(is_palindrome(546645))  # True
print(is_palindrome(421987))  # False
print(is_palindrome(12321))   # True