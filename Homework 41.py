# Завдання 1

products = input("Введіть товари через кому: ")
product_list = [p.strip() for p in products.split(',')]
unique_list = list(set(product_list))

print(unique_list)


# Завдання 2

received = ["Оля", "Іван", "Марія", "Петро"]
used = ["Іван", "Марія", "Сергій"]


def analyze_coupons(received: list, used: list):
    """
    Порівнює списки клієнтів, які отримали купони та які ними скористались.

    :param received: список клієнтів, які отримали купон
    :param used: список клієнтів, які скористались купоном
    :return: None, виводить інформацію на екран
    """
    received_set = set(received)
    used_set = set(used)

    # Ті, хто отримав купон, але не скористався
    not_used = received_set - used_set
    print(f"Клієнти, які отримали купон, але не скористались: {list(not_used)}")
    print(f"Кількість: {len(not_used)}\n")

    # Ті, хто скористався купоном, але не отримував його (шахраї)
    fraudsters = used_set - received_set
    print(f"Шахраї (скористались без купона): {list(fraudsters)}")
    print(f"Кількість: {len(fraudsters)}")

analyze_coupons(received, used)
