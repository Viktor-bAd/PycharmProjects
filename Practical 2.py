# Завдання 1

names = set()  # множина для унікальних імен

while True:
    name = input("Введіть ім'я (порожній рядок для завершення): ").strip()
    if name == "":
        break
    if name in names:
        print(f"Ім'я '{name}' вже введене!")
    else:
        names.add(name)

print(f"Кількість унікальних людей: {len(names)}")


# Завдання 2

all_students = ["Оля", "Іван", "Марія", "Петро", "Сергій"]
group1 = ["Оля", "Іван"]
group2 = ["Марія", "Іван"]


def check_two_groups(all_students: list, group1: list, group2: list):
    """
    Перевіряє два списки груп студентів:
    - знаходить студентів, які одночасно в обох групах
    - знаходить студентів, яких забули (немає в жодній групі)

    :param all_students: список усіх студентів
    :param group1: список студентів першої групи
    :param group2: список студентів другої групи
    :return: None, виводить результати на екран
    """
    # Перевірка на дублікати між групами
    duplicates = set(group1) & set(group2)
    if duplicates:
        print(f"Студенти, які є в обох групах одночасно: {list(duplicates)}")
    else:
        print("Дублікатів студентів між групами немає.")

    # Перевірка на забутих студентів
    in_groups = set(group1) | set(group2)
    forgotten = set(all_students) - in_groups
    if forgotten:
        print(f"Студенти, про яких забули: {list(forgotten)}")
    else:
        print("Жодного забутого студента немає.")


check_two_groups(all_students, group1, group2)


# Завдання 3

# Словник з цінами за кг
prices = {"яблуко": 40, "банан": 30, "груша": 50, "апельсин": 35}


product = input("Введіть назву продукту: ").strip()

if product in prices:
    weight = float(input("Введіть вагу у кг: "))
    total = prices[product] * weight
    print(f"Загальна ціна за {weight} кг {product} становить {total} грн.")
else:
    print("Такого продукту немає у магазині.")
