from typing import Literal, Optional

# Тип для символів на сітці
CROSS = "X"
ZERO = "O"
EMPTY = "Empty"  # порожня клітинка
Symbol = Literal["X", "O"]
Cell = Literal["X", "O", "Empty"]  # "Empty" — порожня клітинка


def create_grid(size: int = 3) -> list[list[Cell]]:
    """
    Створює і повертає порожню сітку для гри «Хрестики-нулики».

    :param size: int - Розмір квадратної сітки (типово 3x3)
    :return: list[list[Cell]] - Двовимірний список, що представляє ігрове поле.
             Кожна клітинка містить "X", "O" або EMPTY.
    """
    grid = []

    for _ in range(size):
        row = [EMPTY] * size
        grid.append(row)

    return grid


print(create_grid(3))


def print_grid(grid: list[list[Cell]]) -> None:
    """
    Виводить поточний стан сітки на екран у зручному для читання вигляді.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: None
    """
    size = len(grid)

    for i in range(size):
        # Виводимо рядок з клітинками (порожні клітинки показуємо як пробіл)
        print(" " + " | ".join(cell if cell != EMPTY else " " for cell in grid[i]) + " ")

        # Виводимо роздільник (крім останнього рядка)
        if i < size - 1:
            print("---+" * (size - 1) + "---")


def add_symbol_to_grid(
    grid: list[list[Cell]],
    row: int,
    col: int,
    symbol: Symbol
) -> bool:
    """
    Додає новий символ на сітку за вказаними координатами.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :param row: int - Індекс рядка (0-based).
    :param col: int - Індекс стовпчика (0-based).
    :param symbol: Symbol - Символ гравця ("X" або "O").
    :return: bool - True, якщо хід успішний (клітинка була вільна),
                    False, якщо клітинка вже зайнята або координати некоректні.
    """
    size = len(grid)

    # 1. Перевірка меж
    if row < 0 or row >= size or col < 0 or col >= size:
        return False

    # 2. Перевірка, чи клітинка порожня
    if grid[row][col] != EMPTY:
        return False

    # 3. Додаємо символ
    grid[row][col] = symbol
    return True


def ask_user_move(player_name: str, grid: list[list[Cell]]) -> tuple[int, int]:
    """
    Запитує у користувача, куди поставити новий символ.

    Повинна:
    - запитати координати (рядок і стовпчик),
    - перевірити, що клітинка вільна,
    - у разі помилки (зайнята/некоректна) — попросити ввести ще раз.

    :param player_name: str - Ім'я поточного гравця (наприклад, "Гравець X").
    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: tuple[int, int] - Пара (row, col) з коректними координатами для ходу.
    """
    size = len(grid)

    while True:
        try:
            print(f"{player_name}, введіть координати (рядок і стовпчик):")

            row = int(input("Рядок (0 - {}): ".format(size - 1)))
            col = int(input("Стовпчик (0 - {}): ".format(size - 1)))

            # Перевірка меж
            if row < 0 or row >= size or col < 0 or col >= size:
                print(" Координати поза межами поля. Спробуйте ще раз.")
                continue

            # Перевірка, чи клітинка вільна
            if grid[row][col] != EMPTY:
                print("Клітинка вже зайнята. Оберіть іншу.")
                continue

            # Все добре
            return row, col

        except ValueError:
            print("Введіть, будь ласка, саме числа.")


def check_winner(grid: list[list[Cell]]) -> Optional[Symbol]:
    """
    Перевіряє, чи є переможець на поточній сітці.

    Перевіряються:
    - усі рядки,
    - усі стовпці,
    - дві діагоналі (головна і побічна).

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: Optional[Symbol] - "X", якщо виграв хрестик,
                                "O", якщо виграв нулик,
                                None, якщо переможця ще немає.
    """
    size = len(grid)

    # 1. Перевірка рядків
    for row in grid:
        if row[0] != EMPTY and all(cell == row[0] for cell in row):
            return row[0]

    # 2. Перевірка стовпців
    for col in range(size):
        first = grid[0][col]

        if first != EMPTY and all(grid[row][col] == first for row in range(size)):
            return first

    # 3. Головна діагональ
    first = grid[0][0]
    if first != EMPTY and all(grid[i][i] == first for i in range(size)):
        return first

    # 4. Побічна діагональ
    first = grid[0][size - 1]
    if first != EMPTY and all(grid[i][size - 1 - i] == first for i in range(size)):
        return first

    # 5. Переможця немає
    return None


def has_empty_cells(grid: list[list[Cell]]) -> bool:
    """
    Перевіряє, чи є на сітці ще вільні (порожні) клітинки.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: bool - True, якщо є хоч одна порожня клітинка,
                    False, якщо поле повністю заповнене.
    """
    for row in grid:
        for cell in row:
            if cell == EMPTY:
                return True

    return False


def is_game_over(grid: list[list[Cell]]) -> bool:
    """
    Перевіряє, чи гра завершена.

    Гра завершується, якщо:
    - є переможець, або
    - немає вільних клітинок (нічия).

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: bool - True, якщо гра завершена, False інакше.
    """
    if check_winner(grid) is not None:
        return True

    if not has_empty_cells(grid):
        return True

    return False


def switch_player(player: Symbol) -> Symbol:
    """
    Змінює поточного гравця.

    :param player: Symbol - Поточний символ гравця ("X" або "O").
    :return: Symbol - Інший символ ("O" якщо був "X", і навпаки).
    """
    if player == "X":
        return "O"
    else:
        return "X"


def main() -> None:
    """
    Головна функція. Організовує всю роботу гри та запускає програму.

    Алгоритм:
    1. Створити порожню сітку.
    2. Встановити стартового гравця (наприклад, "X").
    3. У циклі:
       - вивести сітку;
       - запитати хід у поточного гравця;
       - додати символ до сітки;
       - перевірити, чи є переможець;
       - перевірити, чи ще є вільні клітинки;
       - при завершенні гри вивести результат (хто виграв або нічия);
       - переключити гравця.
    """
    size = 3
    grid = create_grid(size)

    current_player: Symbol = "X"

    while True:
        print_grid(grid)
        print()

        row, col = ask_user_move(f"Гравець {current_player}", grid)
        add_symbol_to_grid(grid, row, col, current_player)

        winner = check_winner(grid)
        if winner is not None:
            print_grid(grid)
            print(f"🎉 Переміг гравець {winner}!")
            break

        if not has_empty_cells(grid):
            print_grid(grid)
            print("🤝 Нічия! Поле повністю заповнене.")
            break

        # Перемикаємо гравця
        current_player = switch_player(current_player)


if __name__ == "__main__":
    main()