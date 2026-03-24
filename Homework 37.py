import random

# ---------------------------
# Константи гри
# ---------------------------

questions: list[str] = [
    "Який твій найбільший страх?",
    "Кого ти останнім часом обговорював?",
    "Яка твоя найбільша таємниця?",
    "Чи подобається тобі хтось зараз?",
    "Який найсмішніший випадок з тобою траплявся?",
]

dares: list[str] = [
    "Заспівай пісню.",
    "Зроби 10 присідань.",
    "Розкажи жарт.",
    "Станцюй 30 секунд.",
    "Зателефонуй другові і скажи щось смішне.",
]


def get_player_names() -> list[str]:
    """
    Запитує імена гравців у користувача та повертає їх у вигляді списку.

    :return: List[str] - список імен гравців
    """
    """
    Запитує імена гравців у користувача та повертає їх у вигляді списку.

    :return: List[str] - список імен гравців
    """
    players: list[str] = []

    # 1. Запитуємо кількість гравців
    count = int(input("Скільки буде гравців? "))

    # 2. Запитуємо ім'я кожного гравця
    for i in range(count):
        name = input(f"Введіть ім'я гравця {i + 1}: ")
        players.append(name)

    # 3. Повертаємо список
    return players


def ask_truth_or_dare(player: str) -> str:
    """
    Запитує у гравця, що він обирає: "Правда" чи "Дія".

    :param player: str - ім'я гравця
    :return: str - рядок з вибором гравця ("правда" або "дія")
    """
    while True:
        # 1. Запитуємо вибір
        choice = input(f"{player}, ти обираєш 'Правда' чи 'Дія'? ")

        # 2. Нормалізуємо введення
        choice = choice.strip().lower()

        # 3. Перевіряємо коректність
        if choice in ("правда", "дія"):
            return choice
        else:
            print("Будь ласка, введіть тільки 'Правда' або 'Дія'.")


def ask_truth_question(player: str) -> None:
    """
    Випадковим чином вибирає одне запитання зі списку `questions`
    та задає його гравцеві.

    :param player: str - ім'я гравця
    :return: None
    """
    # 1. Перевіряємо, чи список не порожній
    if not questions:
        print("Список запитань порожній.")
        return

    # 2. Вибираємо випадкове запитання
    question = random.choice(questions)

    # 3. Виводимо запитання
    print(f"\n{player}, твоє питання:")
    print(question)

    # 4. Отримуємо відповідь (можемо просто зберегти або проігнорувати)
    answer = input("Твоя відповідь: ")

    # Можна просто нічого не робити з відповіддю,
    # або вивести підтвердження
    print("Дякую за чесність")


def perform_dare(player: str) -> None:
    """
    Випадковим чином вибирає одне завдання зі списку `dares`
    та пропонує гравцеві його виконати.

    :param player: str - ім'я гравця
    :return: None
    """
    # 1. Перевіряємо, чи список не порожній
    if not dares:
        print("Список завдань порожній.")
        return

    # 2. Вибираємо випадкове завдання
    dare = random.choice(dares)

    # 3. Виводимо завдання
    print(f"\n{player}, твоє завдання:")
    print(dare)

    # 4. Чекаємо підтвердження виконання
    input("Натисни Enter після виконання завдання...")

    print("Молодець")


def play_game(players: list[str]) -> None:
    """
    Керує ходом гри "Правда або Дія" для переданого списку гравців.

    :param players: List[str] - список імен гравців
    :return: None
    """
    if not players:
        print("Немає гравців для гри.")
        return

    round_number = 1

    while True:
        print(f"\n===== Раунд {round_number} =====")

        # Проходимо по кожному гравцю
        for player in players:
            choice = ask_truth_or_dare(player)

            if choice == "правда":
                ask_truth_question(player)
            elif choice == "дія":
                perform_dare(player)

        # Після завершення раунду
        print(f"\nРаунд {round_number} завершено!")

        # Запитуємо чи продовжувати
        again = input("Бажаєте продовжити гру? (так/ні): ").strip().lower()

        if again != "так":
            print("Гру завершено. Дякуємо за участь!")
            break

        round_number += 1


def main() -> None:
    """
    Точка входу в програму. Ініціалізує гру та запускає її.

    :return: None
    """
    # 1. Отримуємо список гравців
    players = get_player_names()

    # 2. Запускаємо гру
    play_game(players)


if __name__ == "__main__":
    # Приклад використання:
    # Запуск гри з консолі.
    main()
