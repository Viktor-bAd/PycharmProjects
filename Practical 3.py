# Завдання 1


products = ["яблуко", "банан", "груша", "апельсин", "ківі"]

try:
    index = int(input("Введіть індекс товару: "))
    print("Товар:", products[index])
except ValueError:
    print("Помилка: потрібно ввести ціле число.")
except IndexError:
    print("Помилка: такого індексу немає у списку.")


# Завдання 2


def get_age():
    """
    Запитує у користувача вік та повертає його.
    Якщо вік менше 0 або більше 130 — викликає ValueError.
    """
    age = int(input("Введіть ваш вік: "))

    if age < 0 or age > 130:
        raise ValueError("Неправильний вік!")

    return age


try:
    user_age = get_age()
    print("Ваш вік:", user_age)
except ValueError as e:
    print("Помилка:", e)


# Завдання 3


def get_phone():
    """
    Запитує у користувача номер телефону.
    Повертає номер, якщо він правильний.
    Якщо номер не починається з +038 або має не 11 символів,
    викликає виняток ValueError.
    """
    phone = input("Введіть номер телефону: ")

    if not phone.startswith("+380"):
        raise ValueError("Невірний номер телефону!")
    if len(phone) != 11:
        raise ValueError("Невірний номер телефону!")
    return phone


try:
    number = get_phone()
    print("Ваш номер:", number)
except ValueError as e:
    print("Помилка:", e)


# Завдання 4

categories = {
    "фрукти": {"яблуко", "банан", "апельсин"},
    "солодке": {"шоколад", "банан", "печиво"},
    "корисне": {"яблуко", "банан", "горіхи"},
}

try:
    c1 = input("Введіть першу категорію: ")
    c2 = input("Введіть другу категорію: ")

    products = categories[c1] & categories[c2]

    print("Товари в обох категоріях:", products)

except KeyError:
    print("Помилка: такої категорії не існує.")
