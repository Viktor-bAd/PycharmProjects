import math


def temperature(
    T_env: float,
    T0: float,
    t: float,
    k: float = 0.05
) -> float:
    """
    Обчислює температуру води через t секунд
    за законом охолодження Ньютона.

    :param T_env: температура в холодильнику
    :param T0: початкова температура води
    :param t: час у секундах
    :param k: коефіцієнт охолодження (за замовчуванням 0.05)
    :return: температура через t секунд
    """
    return T_env + (T0 - T_env) * math.exp(-k * t)

#Приклад використання
result = temperature(T_env=4, T0=25, t=60)
print(f"Температура через 60 секунд: {result:.2f} °C")


import time


def get_name(show_time: bool = False) -> str:
    """
    Запитує у користувача ім'я та повертає його.
    Якщо show_time = True — виводить час роботи функції.

    :param show_time: чи показувати час виконання
    :return: ім'я користувача
    """
    start_time = time.time()  # Початок вимірювання

    name = input("Введіть ваше ім'я: ")

    end_time = time.time()  # Кінець вимірювання

    if show_time:
        print(f"Час роботи функції: {end_time - start_time:.6f} секунд")

    return name

#Приклад використання
user_name = get_name(show_time=True)
print("Привіт,", user_name)


from date_utils import days_until_deadline


def main():
    deadline = input("Введіть дату дедлайну (YYYY-MM-DD): ")

    days_left = days_until_deadline(deadline)

    print(f"До дедлайну залишилось: {days_left} днів")

    if days_left < 0:
        print("Дедлайн вже минув ")
    elif days_left < 7:
        print("Менше тижня до дедлайну!")
    else:
        print("Час ще є")


if __name__ == "__main__":
    main()


