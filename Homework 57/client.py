import requests

URL = "http://127.0.0.1:8000"


def get_movie():
    movie_id = input("ID фільму: ")

    response = requests.get(f"{URL}/movies/{movie_id}")

    print(response.json())


def add_movie():
    movie = {
        "id": int(input("ID: ")),
        "title": input("Назва: "),
        "director": input("Режисер: "),
        "year": int(input("Рік: "))
    }

    response = requests.post(f"{URL}/movies", json=movie)

    print(response.json())


def delete_movie():
    movie_id = input("ID фільму: ")

    response = requests.delete(f"{URL}/movies/{movie_id}")

    print(response.json())


while True:
    print("\n1. Отримати фільм")
    print("2. Додати фільм")
    print("3. Видалити фільм")
    print("4. Вийти")

    choice = input("Вибір: ")

    if choice == "1":
        get_movie()

    elif choice == "2":
        add_movie()

    elif choice == "3":
        delete_movie()

    elif choice == "4":
        break
