import threading


numbers = []


def input_numbers():
    print("Вводьте числа:")

    while True:
        num = input("Число: ")

        if num == "":
            break

        numbers.append(float(num))


def calculate_sum():
    total = sum(numbers)
    print(f"Список чисел: {numbers}")
    print(f"Сума: {total}")


def calculate_average():
    if len(numbers) > 0:
        avg = sum(numbers) / len(numbers)
        print(f"Середнє арифметичне: {avg}")
    else:
        print("Список порожній.")


t1 = threading.Thread(target=input_numbers)
t2 = threading.Thread(target=calculate_sum)
t3 = threading.Thread(target=calculate_average)


t1.start()
t1.join()

t2.start()
t3.start()

t2.join()
t3.join()
