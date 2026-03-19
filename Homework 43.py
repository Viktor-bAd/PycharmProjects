# Завдання 1

rates = {
    "грн": 1,
    "долар": 40,
    "євро": 42
}


from_currency = input("З якої валюти: ")
amount = float(input("Сума: "))
to_currency = input("В яку валюту: ")

if from_currency in rates and to_currency in rates:

    uah = amount * rates[from_currency]


    result = uah / rates[to_currency]

    print(f"Результат: {result}")
else:
    print("Невідома валюта.")


# Завдання 2

def analyze_workers(office: set, remote: set):
    """
    Аналізує працівників, які працюють в офісі та віддалено.

    :param office: множина працівників в офісі
    :param remote: множина віддалених працівників
    :return: None, виводить інформацію на екран
    """
    # усі працівники
    all_workers = office | remote
    print("Усі працівники:", all_workers)

    # ті, хто працює і там, і там
    both = office & remote
    print("Працюють і в офісі, і віддалено:", both)

    # відсоток
    if len(all_workers) > 0:
        percent = len(both) / len(all_workers) * 100
    else:
        percent = 0

    print(f"Відсоток таких працівників: {percent:.2f}%")


office = {"Іван", "Оля", "Марія"}
remote = {"Оля", "Петро", "Іван"}

analyze_workers(office, remote)