# Завдання 1

def get_password():
    """
    Запитує у користувача пароль.
    Повертає пароль, якщо він коректний.
    Якщо пароль менше 8 символів або всі символи однакові —
    викликає ValueError.
    """
    password = input("Введіть пароль: ")

    # перевірка довжини
    if len(password) < 8:
        raise ValueError("Пароль має містити не менше 8 символів!")

    # перевірка на однакові символи
    if len(set(password)) == 1:
        raise ValueError("Пароль не може складатися з однакових символів!")

    return password


try:
    user_password = get_password()
    print("Пароль прийнято:", user_password)
except ValueError as e:
    print("Помилка:", e)


# Задвання 2

# словник логінів і паролів
users = {
    "admin": "1234",
    "user": "qwerty",
    "ivan": "pass123"
}


def login_user(data: dict):
    """
    Запитує логін і пароль у користувача.
    Якщо логін відсутній або пароль невірний —
    викликає ValueError.
    """
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if login not in data:
        raise ValueError("Користувача не знайдено.")

    if data[login] != password:
        raise ValueError("Невірний пароль.")

    return login


try:
    user = login_user(users)
    print(f"Вхід виконано успішно. Вітаємо, {user}!")
except ValueError as e:
    print("Помилка:", e)
