import random

# Введення користувача
user_input = input("Введіть числа через кому: ")

# Створюємо множину користувача
user_set = set(int(num) for num in user_input.split(",") if num)

# Створюємо випадкову множину (12 чисел)
random_set = set(random.randint(1, 30) for _ in range(12))

# Максимальне, мінімальне та кількість
print("Максимальне число:", max(user_set))
print("Мінімальне число:", min(user_set))
print("Кількість чисел:", len(user_set))


# Унікальні числа користувача
unique_numbers = user_set.difference(random_set)
print("Унікальні числа користувача:", unique_numbers)

# Спільні числа
common_numbers = user_set.intersection(random_set)
print("Спільні числа:", common_numbers)

# Усі числа з обох множин
all_numbers = user_set.union(random_set)
print("Усі числа:", all_numbers)


guests_list = ["Оля", "Іван", "Марія", "Оля", "Іван"]

def send_invitations(guests: list[str], event_name: str) -> None:
    """
    Виводить запрошення для кожного гостя лише один раз.

    :param guests: список гостей (можуть повторюватись)
    :param event_name: назва події
    """
    unique_guests = set(guests)  # прибираємо повтори

    for guest in unique_guests:
        print(f"Шановний(а) {guest}, запрошуємо Вас на подію '{event_name}'!")

send_invitations(guests_list, "День народження")


person1 = ["молоко", "хліб", "яйця", "сир"]
person2 = ["хліб", "масло", "яйця", "кава"]

def compare_shopping_lists(list1: list[str], list2: list[str]) -> None:
    """
    Порівнює два списки товарів та виводить:
    - Товари, які можна купити разом
    - Товари, які потрібні лише першій людині
    - Товари, які потрібні лише другій людині

    :param list1: список товарів першої людини
    :param list2: список товарів другої людини
    """

    set1 = set(list1)
    set2 = set(list2)

    common_products = set1.intersection(set2)
    only_first = set1.difference(set2)
    only_second = set2.difference(set1)

    print("Товари, які можна купити разом:", common_products)
    print("Товари, які потрібні лише першій людині:", only_first)
    print("Товари, які потрібні лише другій людині:", only_second)

compare_shopping_lists(person1, person2)


registered = ["Оля", "Іван", "Марія", "Андрій"]
paid = ["Іван", "Марія", "Петро"]
confirmed = ["Марія", "Іван", "Сергій"]

def analyze_participants(registered: list[str],
                         paid: list[str],
                         confirmed: list[str]) -> None:
    """
    Аналізує списки учасників конференції та виводить інформацію:

    :param registered: список зареєстрованих
    :param paid: список тих, хто оплатив участь
    :param confirmed: список тих, хто підтвердив присутність
    """

    reg_set = set(registered)
    paid_set = set(paid)
    conf_set = set(confirmed)

    # Зареєстровані, але не оплатили
    not_paid = reg_set.difference(paid_set)

    # Підтвердили, але не зареєстровані
    confirmed_not_registered = conf_set.difference(reg_set)

    # Оплатили, але не підтвердили
    paid_not_confirmed = paid_set.difference(conf_set)

    # Зареєструвались і оплатили
    registered_and_paid = reg_set.intersection(paid_set)

    # Пройшли всі 3 етапи
    all_three = reg_set.intersection(paid_set, conf_set)

    print("Зареєструвались, але не оплатили:", not_paid)
    print("Підтвердили, але не зареєстровані:", confirmed_not_registered)
    print("Оплатили, але не підтвердили:", paid_not_confirmed)
    print("Зареєструвались і оплатили:", registered_and_paid)
    print("Пройшли всі 3 етапи:", all_three)

analyze_participants(registered, paid, confirmed)


