dict1 = {"яблука": 3, "банани": 2}
dict2 = {"банани": 4, "апельсини": 5}


def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Об'єднує два словники в один.

    Якщо ключі співпадають, то їх значення додаються.
    Якщо ключ є лише в одному словнику, він просто
    додається в результат.

    :param dict1: dict - перший словник
    :param dict2: dict - другий словник
    :return: dict - новий словник з об'єднаними даними
    """

    result = {}

    for key in dict1:
        result[key] = dict1[key]

    for key in dict2:
        if key in result:
            result[key] += dict2[key]
        else:
            result[key] = dict2[key]

    return result


print(merge_dicts(dict1, dict2))


data = {"apple": 1, "banana": 2, "orange": 3}


def invert_dict(dict3: dict) -> dict:
    """
    Інвертує словник: міняє місцями ключі та значення.

    :param dict3: dict - початковий словник
    :return: dict - новий словник, де ключі і значення поміняні місцями
    """

    result = {}

    for key in dict3:
        value = dict3[key]
        result[value] = key

    return result


print(invert_dict(data))


def products_prices():
    """
    Дозволяє користувачу вводити назви товарів та їх ціни.
    Дані зберігаються у словнику у форматі: товар -> ціна.

    Якщо товар вводиться повторно, нова ціна додається до
    вже існуючої.

    Ввід завершується, коли користувач вводить порожній рядок.

    Після завершення програма:
    - виводить таблицю "товар – ціна"
    - обчислює та виводить загальну суму всіх товарів
    """

    products = {}

    while True:
        name = input("Введіть назву товару: ")

        if name == "":
            break

        price = int(input("Введіть ціну: "))

        if name in products:
            products[name] += price
        else:
            products[name] = price

    print("Товар - Ціна")
    print("----------------")

    total = 0

    for name in products:
        print(name, "-", products[name])
        total += products[name]

    print("----------------")
    print("Загальна ціна:", total)


products_prices()


text = "Apple banana apple Orange banana apple"


def word_count(text: str, as_frequency: bool = False) -> dict:
    """
    Повертає словник слів з їх кількістю або частотою в тексті.
    Розділення відбувається лише по пробілу.
    Частота повертається у відсотках як ціле число.

    :param text: str - вхідний текст
    :param as_frequency: bool - якщо True, значення словника будуть частотою (%) від загальної кількості слів,
                                якщо False – кількістю повторів
    :return: dict - словник {слово: кількість або частота}
    """

    words = text.split()
    total_words = len(words)
    counts = {}

    for word in words:
        word_lower = word.lower()
        counts[word_lower] = counts.get(word_lower, 0) + 1

    if as_frequency:
        for word in counts:
            counts[word] = int((counts[word] / total_words) * 100)

    return counts


# Кількість повторів
print(word_count(text))


# Частота (%)
print(word_count(text, as_frequency=True))
