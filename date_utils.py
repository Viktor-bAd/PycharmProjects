from datetime import date


def days_until_deadline(deadline_str: str) -> int:
    """
    Отримує дату дедлайну у форматі YYYY-MM-DD
    та повертає кількість днів до дедлайну.

    :param deadline_str: дата у форматі YYYY-MM-DD
    :return: кількість днів до дедлайну
    """
    deadline_date = date.fromisoformat(deadline_str)
    today = date.today()

    delta = deadline_date - today
    return delta.days
