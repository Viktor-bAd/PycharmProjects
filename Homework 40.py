#Завдання 1

cities = ("Київ", "Одеса", "Львів", "Київ", "Харків", "Одеса")

duplicates = set()

for city in cities:
    if cities.count(city) > 1:
        duplicates.add(city)

print(duplicates)


#Завдання 2

t1 = (1, 2, 3, 4, 5, 6)
t2 = (4, 5, 6, 7, 8)

print(tuple(set(t1) - set(t2)))


#Завдання 3

t1 = (1, 2, 3, 4, 5)
t2 = (1, 9, 3, 8, 5)

def same_index_elements(t1: tuple, t2: tuple) -> list:
    """
    Повертає список елементів, які знаходяться на однакових індексах
    у двох кортежах і рівні між собою.

    :param t1: Перший кортеж
    :param t2: Другий кортеж
    :return: Список елементів, що збігаються за значенням і індексом
    """
    result = []

    for a, b in zip(t1, t2):
        if a == b:
            result.append(a)

    return result

print(same_index_elements(t1, t2))