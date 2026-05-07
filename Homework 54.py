import json
import pickle


# --- додати гурт ---
def add_band(bands):
    name = input("Введіть назву гурту: ")

    if name in bands:
        print("Такий гурт вже існує.")
    else:
        bands[name] = []
        print("Гурт додано.")


# --- додати альбом ---
def add_album(bands):
    name = input("Введіть назву гурту: ")

    if name not in bands:
        print("Гурт не знайдено.")
        return

    album = input("Введіть назву альбому: ")
    bands[name].append(album)

    print("Альбом додано.")


# --- зберегти json ---
def save_json(bands, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(bands, f, ensure_ascii=False, indent=4)

    print("Дані збережено у json.")


# --- завантажити json ---
def load_json(filename):
    with open(filename, "a+", encoding="utf-8") as f:
        f.seek(0)
        content = f.read()

        if content:
            return json.loads(content)

    return {}


# --- зберегти pickle ---
def save_pickle(bands, filename):
    with open(filename, "wb") as f:
        pickle.dump(bands, f)

    print("Дані збережено у pickle.")


# --- завантажити pickle ---
def load_pickle(filename):
    with open(filename, "ab+") as f:
        f.seek(0)

        content = f.read()

        if content:
            f.seek(0)
            return pickle.load(f)

    return {}


# --- показати дані ---
def show_bands(bands):
    for band, albums in bands.items():
        print(f"\nГурт: {band}")
        print("Альбоми:")

        for album in albums:
            print("-", album)


# --- меню ---
def menu():
    bands = {}

    while True:
        print("\n1. Додати гурт")
        print("2. Додати альбом")
        print("3. Зберегти через json")
        print("4. Завантажити через json")
        print("5. Зберегти через pickle")
        print("6. Завантажити через pickle")
        print("7. Показати дані")
        print("8. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            add_band(bands)

        elif choice == "2":
            add_album(bands)

        elif choice == "3":
            save_json(bands, "bands.json")

        elif choice == "4":
            bands = load_json("bands.json")
            print("Дані завантажено.")

        elif choice == "5":
            save_pickle(bands, "bands.pkl")

        elif choice == "6":
            bands = load_pickle("bands.pkl")
            print("Дані завантажено.")

        elif choice == "7":
            show_bands(bands)

        elif choice == "8":
            print("Вихід...")
            break

        else:
            print("Невірний вибір.")


menu()
