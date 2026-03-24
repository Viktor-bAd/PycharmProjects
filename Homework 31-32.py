# Завдання 1
def report_for_tax(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)

        if data[1] < 0 or data[2] < 0:
            return "Error: дохід/витрати не можуть бути від’ємними"

        return (
            f"[TAX REPORT]\n"
            f"Year: {data[0]}\n"
            f"Income: {data[1]}\n"
            f"Expenses: {data[2]}\n"
            f"Profit: {data[3]}\n"
            f"Tax: {data[4]}\n"
            f"Tax Rate: {data[5]}\n"
            f"Net Profit: {data[6]}"
        )

    return wrapper


def report_for_ministry(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return (
            f"[MINISTRY REPORT]\n"
            f"Year: {data[0]} | Income: {data[1]} | Expenses: {data[2]} | Net Profit: {data[6]}"
        )

    return wrapper


def report_for_statistics(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return {
            "year": data[0],
            "income": data[1],
            "expenses": data[2],
            "profit": data[3],
        }

    return wrapper


def build_finance_report(year, income, expenses, tax_rate):
    income = float(income)
    expenses = float(expenses)
    tax_rate = float(tax_rate)

    profit = income - expenses
    tax = max(0.0, profit) * tax_rate
    net_profit = profit - tax

    return [int(year), income, expenses, profit, tax, tax_rate, net_profit]


@report_for_ministry
def ministry_report(year, income, expenses, tax_rate):
    return build_finance_report(year, income, expenses, tax_rate)


@report_for_statistics
def statistics_report(year, income, expenses, tax_rate):
    return build_finance_report(year, income, expenses, tax_rate)


@report_for_tax
def tax_report(year, income, expenses, tax_rate):
    return build_finance_report(year, income, expenses, tax_rate)


def main():
    year = 2026
    income = 1_500_000
    expenses = 900_000
    tax_rate = 0.05

    print("Звіт для міністерства:")
    print(ministry_report(year, income, expenses, tax_rate))
    print()

    print("Звіт для статистики:")
    print(statistics_report(year, income, expenses, tax_rate))
    print()

    print("Звіт для податкової:")
    print(tax_report(year, income, expenses, tax_rate))


if __name__ == "__main__":
    main()

# завдання 2

import datetime


def audit(func):
    def wrapper(user, target, value=None):
        timestamp = datetime.datetime.now()  # поточний час

        if value is not None:
            result = func(user, target, value)
        else:
            result = func(user, target)

        print(timestamp, user, func.__name__, target, value)

        return result

    return wrapper


@audit
def create_data(user, data_name, value):
    print(user, "створив", data_name, "зі значенням", value)
    return True


@audit
def delete_data(user, data_name):
    print(user, "видалив", data_name)
    return True


@audit
def update_data(user, data_name, new_value):
    print(user, "оновив", data_name, "на", new_value)
    return True


def main():
    create_data("Alice", "balance", 1000)
    delete_data("Bob", "old_report")
    update_data("Charlie", "balance", 1200)


if __name__ == "__main__":
    main()

# Завдання 3

import time


# Декоратор для обмеження частоти
def rate_limit(max_calls, period_seconds):
    """
    max_calls: максимально дозволена кількість викликів
    period_seconds: проміжок часу у секундах
    """
    call_times = {}

    def decorator(func):
        def wrapper(user, *args):
            now = time.time()
            if user not in call_times:
                call_times[user] = []

            call_times[user] = [t for t in call_times[user] if now - t < period_seconds]

            if len(call_times[user]) >= max_calls:
                print(user, "перевищив ліміт викликів для", func.__name__)
                return None

            call_times[user].append(now)

            #
            return func(user, *args)

        return wrapper

    return decorator


@rate_limit(max_calls=2, period_seconds=5)  # не більше 2 викликів за 5 секунд
def get_data(user, data_name):
    print(user, "отримав дані", data_name)
    return f"Data for {data_name}"


@rate_limit(max_calls=1, period_seconds=10)  # не більше 1 виклику за 10 секунд
def update_data(user, data_name, value):
    print(user, "оновив дані", data_name, "на", value)
    return True


def main():
    get_data("Alice", "balance")
    get_data("Alice", "balance")
    get_data("Alice", "balance")  # тут перевищить ліміт

    update_data("Bob", "balance", 1000)
    update_data("Bob", "balance", 2000)  # тут перевищить ліміт

    time.sleep(5)
    get_data("Alice", "balance")  # працює знову


if __name__ == "__main__":
    main()
