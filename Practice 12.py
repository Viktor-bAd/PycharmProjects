import json
import pickle


JSON_FILE: str = "products.json"
PICKLE_FILE: str = "products.pkl"


def add_product(products: list[str]) -> None:
    name = input("Введіть назву товару: ")
    products.append(name)
    print(f"Товар '{name}' додано.")


def show_products(products: list[str]) -> None:
    if not products:
        print("Список товарів порожній.")
    else:
        print("\n--- Список товарів ---")
        for i, product in enumerate(products, 1):
            print(f"{i}. {product}")


def save_json(products: list[str]) -> None:
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False, indent=4)
    print(f"Дані збережено у {JSON_FILE} (JSON).")


def save_pickle(products: list[str]) -> None:
    with open(PICKLE_FILE, "wb") as file:
        pickle.dump(products, file)
    print(f"Дані збережено у {PICKLE_FILE} (Pickle).")


def load_json() -> list[str]:
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    print("Дані завантажено з JSON.")
    return data


def load_pickle() -> list[str]:
    with open(PICKLE_FILE, "rb") as file:
        data = pickle.load(file)
    print("Дані завантажено з Pickle.")
    return data


def main() -> None:
    products = []

    while True:
        print("\n1. Додати товар")
        print("2. Показати список")
        print("3. Зберегти (JSON)")
        print("4. Зберегти (Pickle)")
        print("5. Завантажити (JSON)")
        print("6. Завантажити (Pickle)")
        print("0. Вихід")

        choice: str = input("Оберіть дію: ")

        if choice == "1":
            add_product(products)
        elif choice == "2":
            show_products(products)
        elif choice == "3":
            save_json(products)
        elif choice == "4":
            save_pickle(products)
        elif choice == "5":
            products = load_json()
        elif choice == "6":
            products = load_pickle()
        elif choice == "0":
            break
        else:
            print("Невірний вибір!")


main()


class Student:
    def __init__(self, name: str, specialization: str):
        self.name = name
        self.specialization = specialization
        self.grades: list[int] = []

    def add_grade(self, grade: int) -> None:
        self.grades.append(grade)

    def get_average(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def show_info(self) -> None:
        avg = self.get_average()
        print(f"Студент: {self.name}")
        print(f"Спеціалізація: {self.specialization}")
        print(f"Середня оцінка: {avg:.2f}")
        print("-" * 20)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "specialization": self.specialization,
            "grades": self.grades
        }


students = [
    Student("Олександр", "Python Developer"),
    Student("Марія", "Data Science"),
    Student("Іван", "Cybersecurity")
]

students[0].add_grade(95); students[0].add_grade(88)
students[1].add_grade(100); students[1].add_grade(92)
students[2].add_grade(85); students[2].add_grade(70)

with open("students.pkl", "wb") as f:
    pickle.dump(students, f)
print("Дані збережено через Pickle.")

with open("students.json", "w", encoding="utf-8") as f:
    json_data = [s.to_dict() for s in students]
    json.dump(json_data, f, ensure_ascii=False, indent=2)

with open("students.pkl", "rb") as f:
    loaded_pickle = pickle.load(f)
for s in loaded_pickle:
    s.show_info()

with open("students.json", "r", encoding="utf-8") as f:
    loaded_json_data = json.load(f)

loaded_json_students: list[Student] = []
for item in loaded_json_data:
    s = Student(item["name"], item["specialization"])
    s.grades = item["grades"]
    loaded_json_students.append(s)

for s in loaded_json_students:
    s.show_info()


# Реалізуйте телефонну книгу.
# Контакт містить:
# ім’я
# телефон
# email
# Функціонал:
# додати контакт
# видалити контакт
# знайти контакт за ім’ям
# показати всі контакти
# зберегти/завантажити через json
# зберегти/завантажити через pickle
# Віктор: {phone: 0935075803
#          email: viktor.bad@gmail.com}
#
# Оксана: {phone: 0930772315
#          email: oksana@gmail.com}
import json

JSON_FILE = "book.json"
PICKLE_FILE = "book.pickle"

def add_contact(book: dict[str, dict[str, str]]) -> None:
    name = input('Ввести імʼя')
    phone = input('Ввести телефон')
    email = input("Ввести емеил")
    book[name] = {
        "phone": phone,
        "email": email
    }

def save_json(book: dict[str, dict[str, str]]) -> None:
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(book, file, ensure_ascii=False, indent=2)


book = {}
add_contact(book)
save_json(book)
#
#
#
