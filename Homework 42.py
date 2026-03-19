
def deposit(bank: dict):
    """
    Поповнення рахунку.
    Якщо клієнта немає — створює його.
    """
    name = input("Введіть ім'я клієнта: ")
    amount = float(input("Введіть суму для поповнення: "))

    if name in bank:
        bank[name] += amount
    else:
        bank[name] = amount

    print(f"Баланс {name}: {bank[name]}")


def withdraw(bank: dict):
    """
    Зняття коштів з рахунку.
    """
    name = input("Введіть ім'я клієнта: ")

    if name not in bank:
        print("Клієнта не знайдено.")
        return

    amount = float(input("Введіть суму для зняття: "))

    if bank[name] < amount:
        print("Недостатньо коштів.")
    else:
        bank[name] -= amount
        print(f"Баланс {name}: {bank[name]}")


def main():
    """
    Основна функція для роботи з програмою.
    """
    bank = {}

    while True:
        print("\n1 - Поповнити рахунок")
        print("2 - Зняти кошти")
        print("3 - Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            deposit(bank)
        elif choice == "2":
            withdraw(bank)
        elif choice == "3":
            print("Завершення роботи.")
            break
        else:
            print("Невірний вибір.")



main()