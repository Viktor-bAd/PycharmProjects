# Завдання 1

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

start = min(a, b)
end = max(a, b)

total = sum(range(start, end + 1))

print("Сума діапазону чисел:", total)


# Завдання 2

total = 0

for number in range(1, 101):
    if number % 2 == 0:
        total += number

print("Сума всіх парних чисел від 1 до 100:", total)


# Завдання 3

text = input("Введіть рядок: ")

for letter in text:
    print(letter)


# Завдання 4

import random

numbers = [random.randint(1, 100) for _ in range(10)]

even_numbers = [num for num in numbers if num % 2 == 0]

print(f"Випадковий список: {numbers}")
print(f"Тільки парні: {even_numbers}")


# Завдання 5

def get_capitalized_strings():
    """
    Повертає список рядків, які починаються з великої літери.
    """
    user_input = input("Введіть слова через пробіл: ")

    strings = user_input.split()

    result = [s for s in strings if s and s[0].isupper()]

    return result


capitalized_list = get_capitalized_strings()
print(f"Ваш список: {capitalized_list}")


# Завдання 6

def filter_python_lines():
    """Зчитує введений користувачем рядок, розбиває його на окремі речення
    та повертає список лише тих, що містять ключове слово "Python"."""

    user_input = input("Введіть речення, розділяючи їх крапкою з комою (;): ")

    lines = user_input.split(';')

    result = [line.strip() for line in lines if "Python" in line]

    return result


python_list = filter_python_lines()
print(f"Список речень, що містять 'Python': {python_list}")


# Завдання 7

def dictionary_app():
    my_dict = {}

    while True:
        print("\n--- СЛОВНИК ---")
        print("1. Додати слово")
        print("2. Видалити слово")
        print("3. Шукати слово")
        print("4. Вийти")

        choice = input("Оберіть дію (1-4): ")

        if choice == '1':
            word = input("Введіть слово: ").strip()
            definition = input(f"Введіть визначення для '{word}': ").strip()
            my_dict[word] = definition
            print(f"Слово '{word}' успішно додано!")

        elif choice == '2':
            word = input("Яке слово видалити?: ").strip()
            if word in my_dict:
                del my_dict[word]
                print(f"Слово '{word}' видалено.")
            else:
                print("Помилка: слово не знайдено у словнику.")

        elif choice == '3':
            word = input("Яке слово шукаємо?: ").strip()
            print(f"Визначення: {my_dict.get(word, 'Слово не знайдено.')}")

        elif choice == '4':
            print("До побачення!")
            break

        else:
            print("Некоректний вибір, спробуйте ще раз.")



dictionary_app()


# Завдання 8

data = [(1, 3), (3, 2), (2, 1)]

sorted_data = sorted(data, key=lambda x: x[1])

print(f"Початковий список: {data}")
print(f"Відсортований список: {sorted_data}")


# Завдання ООП

from datetime import datetime


class User:
    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self._password = password

    def check_password(self, password: str) -> bool:
        return self._password == password


class WebPage:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
        self._publish_date = datetime.now().strftime("%d.%m.%Y %H:%M")

    def show_info(self) -> None:
        print("\n--------------------")
        print(f"Заголовок: {self.title}")
        print(f"Вміст: {self.content}")
        print(f"Дата публікації: {self._publish_date}")

    def edit(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
        print("Сторінку відредаговано!")


class WebSite:
    def __init__(self, name: str, url: str) -> None:
        self.name = name
        self.url = url
        self._pages: list[WebPage] = []

    def add_page(self, page: WebPage) -> None:
        self._pages.append(page)
        print("Сторінку додано!")

    def remove_page(self, title: str) -> None:
        for page in self._pages:
            if page.title == title:
                self._pages.remove(page)
                print("Сторінку видалено!")
                return

        print("Сторінку не знайдено.")

    def edit_page(self, title: str) -> None:
        for page in self._pages:
            if page.title == title:
                new_title: str = input("Новий заголовок: ")
                new_content: str = input("Новий вміст: ")
                page.edit(new_title, new_content)
                return

        print("Сторінку не знайдено.")

    def search_pages(self, keyword: str) -> None:
        found: bool = False

        for page in self._pages:
            if keyword.lower() in page.title.lower() or keyword.lower() in page.content.lower():
                page.show_info()
                found = True

        if not found:
            print("Збігів не знайдено.")

    def show_info(self) -> None:
        print("\n===== ІНФОРМАЦІЯ ПРО САЙТ =====")
        print(f"Назва: {self.name}")
        print(f"URL: {self.url}")
        print(f"Кількість сторінок: {len(self._pages)}")

        if not self._pages:
            print("Сторінок поки немає.")
        else:
            for page in self._pages:
                page.show_info()


users = []
current_user = None
website = None

while True:

    if current_user is None:
        print("\n===== АВТОРИЗАЦІЯ =====")
        print("1. Реєстрація")
        print("2. Вхід")
        print("3. Вихід")

        choice: str = input("Оберіть дію: ")

        if choice == "1":
            login = input("Логін: ")
            password = input("Пароль: ")

            exists: bool = False

            for user in users:
                if user.login == login:
                    exists = True
                    break

            if exists:
                print("Такий користувач вже існує.")
            else:
                users.append(User(login, password))
                print("Реєстрація успішна!")

        elif choice == "2":
            login = input("Логін: ")
            password= input("Пароль: ")

            for user in users:
                if user.login == login and user.check_password(password):
                    current_user = user
                    print("Вхід виконано!")
                    break
            else:
                print("Невірний логін або пароль.")

        elif choice == "3":
            print("До побачення!")
            break

        else:
            print("Невірний вибір.")

    else:
        print(f"\n===== Меню ({current_user.login}) =====")
        print("1. Створити сайт")
        print("2. Додати сторінку")
        print("3. Видалити сторінку")
        print("4. Редагувати сторінку")
        print("5. Пошук сторінок")
        print("6. Переглянути інформацію про сайт")
        print("7. Вийти з акаунта")

        choice = input("Оберіть дію: ")

        if choice == "1":
            name = input("Назва сайту: ")
            url = input("URL сайту: ")

            website = WebSite(name, url)
            print("Сайт створено!")

        elif choice == "2":
            if website is None:
                print("Спочатку створіть сайт.")
            else:
                title: str = input("Заголовок сторінки: ")
                content: str = input("Вміст сторінки: ")

                website.add_page(WebPage(title, content))

        elif choice == "3":
            if website is None:
                print("Спочатку створіть сайт.")
            else:
                title: str = input("Назва сторінки для видалення: ")
                website.remove_page(title)

        elif choice == "4":
            if website is None:
                print("Спочатку створіть сайт.")
            else:
                title: str = input("Назва сторінки для редагування: ")
                website.edit_page(title)

        elif choice == "5":
            if website is None:
                print("Спочатку створіть сайт.")
            else:
                keyword = input("Введіть ключове слово: ")
                website.search_pages(keyword)

        elif choice == "6":
            if website is None:
                print("Сайт ще не створений.")
            else:
                website.show_info()

        elif choice == "7":
            current_user = None
            print("Ви вийшли з акаунта.")

        else:
            print("Невірний вибір.")
