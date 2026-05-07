import random
import json


# --- нова гра ---
def new_game(stats):
    number = random.randint(1, 100)
    attempts = 0

    print("Комп'ютер загадав число від 1 до 100.")

    while True:
        guess = int(input("Введіть число: "))
        attempts += 1

        if guess > number:
            print("Менше")
        elif guess < number:
            print("Більше")
        else:
            print(f"Ви вгадали число за {attempts} спроб!")

            if attempts < 5:
                print("Переміг користувач!")
                stats["wins"] += 1
            else:
                print("Переміг комп'ютер!")
                stats["losses"] += 1

            break


# --- показати результат ---
def show_results(stats):
    print(f"Перемог користувача: {stats['wins']}")
    print(f"Поразок користувача: {stats['losses']}")


# --- зберегти ---
def save_data(stats, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(stats, f)


# --- завантажити ---
def load_data(filename):
    with open(filename, "a+", encoding="utf-8") as f:
        f.seek(0)
        content = f.read()

        if content:
            return json.loads(content)
        else:
            return {"wins": 0, "losses": 0}


# --- меню ---
def menu():
    filename = "game_stats.json"
    stats = load_data(filename)

    while True:
        print("\n1. Нова гра")
        print("2. Показати результати")
        print("3. Зберегти дані")
        print("4. Завантажити дані")
        print("5. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            new_game(stats)

        elif choice == "2":
            show_results(stats)

        elif choice == "3":
            save_data(stats, filename)
            print("Дані збережено.")

        elif choice == "4":
            stats = load_data(filename)
            print("Дані завантажено.")

        elif choice == "5":
            save_data(stats, filename)
            print("Вихід...")
            break

        else:
            print("Невірний вибір.")


menu()
