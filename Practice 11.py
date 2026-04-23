import json


FILE_NAME = "users_data.json"


def load_data() -> dict[str, str]:
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_data(users: dict[str, str]) -> None:
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(users, file, ensure_ascii=False, indent=2)
    print("Дані збережено.")


def add_user(users: dict[str, str]) -> None:
    login = input("Введіть новий логін: ")
    if login in users:
        print("Помилка: користувач вже існує.")
    else:
        password = input("Введіть пароль: ")
        users[login] = password
        print(f"Користувача {login} успішно додано.")


def delete_user(users: dict[str, str]) -> None:
    login = input("Введіть логін для видалення: ")
    if login in users:
        del users[login]
        print(f"Користувача {login} видалено.")
    else:
        print("Користувача не знайдено.")


def change_password(users: dict[str, str]) -> None:
    login = input("Введіть логін: ")
    if login in users:
        new_password = input("Введіть новий пароль: ")
        users[login] = new_password
        print("Пароль оновлено.")
    else:
        print("Користувача не знайдено.")


def login_system(users: dict[str, str]) -> bool:
    login = input("Логін: ")
    password = input("Пароль: ")
    if users.get(login) == password:
        print("Вхід успішний!")
        return True
    print("Невірні дані для входу.")
    return False


def main() -> None:

    users = {}

    while True:
        print(
            "\n1. Завантажити з файлу\n2. Зберегти у файл\n3. Додати\n4. Видалити\n5. Змінити пароль\n6. Увійти\n0. Вихід")
        choice = input("Виберіть дію: ")

        if choice == '1':
            users = load_data()
            print("Дані завантажено.")
        elif choice == '2':
            save_data(users)
        elif choice == '3':
            add_user(users)
        elif choice == '4':
            delete_user(users)
        elif choice == '5':
            change_password(users)
        elif choice == '6':
            login_system(users)
        elif choice == '0':
            break
        else:
            print("Невірний вибір.")



main()

import json


class Cart:
    def __init__(self, user: str):
        self.user = user
        self.items = []
        self.total = 0

    def add(self, item: str, price: float) -> None:
        self.items.append(item)
        self.total += price
        print(f"Додано: {item} (+{price} грн)")

    def delete(self, item: str, price: float) -> None:
        if item in self.items:
            self.items.remove(item)
            self.total -= price
            print(f"Видалено: {item} (-{price} грн)")
        else:
            print(f"Помилка: '{item}' не знайдено в кошику.")

    def info(self) -> None:
        print(f"\nКористувач: {self.user}")
        print(f"Товари: {', '.join(self.items) if self.items else 'порожньо'}")
        print(f"Разом: {self.total} грн\n")

    def save(self, filename: str = "cart.json") -> None:
        data = {
            "user": self.user,
            "items": self.items,
            "total": self.total
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Дані збережено у файл '{filename}'.")

    def load(self, filename: str = "cart.json") -> None:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.user = data["user"]
            self.items = data["items"]
            self.total = data["total"]
        print(f"Дані з файлу '{filename}' завантажено.")


cart = Cart("Віктор")

cart.add("Скейтинг-борд", 2100)
cart.add("Захисний шолом", 850)
cart.info()

cart.save()

another_cart = Cart("Stranger")
another_cart.load()
another_cart.info()
