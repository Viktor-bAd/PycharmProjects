# Завдання 1

items = ["  Milk  ", "bread", "BREAD", "", "  eggs", "Eggs ", "   ", "cheese"]

items = list(map(str.strip, items))

items = list(filter(bool, items))

items = list(map(str.lower, items))

final_items = []
for item in items:
    if item not in final_items:
        final_items.append(item)

print(final_items)


# Завдання 2

students = [
    {"name": "Іра", "age": 17, "avg": 91, "has_debt": False},
    {"name": "Петро", "age": 19, "avg": 73, "has_debt": True},
    {"name": "Оля", "age": 18, "avg": 88, "has_debt": False},
    {"name": "Максим", "age": 20, "avg": 60, "has_debt": False},
]

def make_student_filter(min_avg, max_age, no_debts_only=True, name_startswith=None):
    def predicate(student):
        if student["avg"] < min_avg:
            return False
        if student["age"] > max_age:
            return False
        if no_debts_only and student["has_debt"]:
            return False
        if name_startswith is not None and not student["name"].startswith(name_startswith):
            return False
        return True
    return predicate

filtered_students = filter(
    make_student_filter(min_avg=80, max_age=18, no_debts_only=True),
    students
)

names = []
for s in filtered_students:
    names.append(s["name"])

print(names)


# Завдання 3

nums = [1, -2, 3, 0, 4, -5, 10, 11, 12]

def only_positive(x):
    return x > 0

def only_even(x):
    return x % 2 == 0

def square(x):
    return x * x

def apply_pipeline(data, steps):
    result = data
    for step_type, func in steps:
        if step_type == "map":
            result = list(map(func, result))
        elif step_type == "filter":
            result = list(filter(func, result))
        else:
            raise ValueError("Невідомий тип кроку")
    return result

pipeline = [
    ("filter", only_positive),
    ("filter", only_even),
    ("map", square)
]

positive = apply_pipeline(nums, [("filter", only_positive)])
print("Позитивні:", positive)

even = apply_pipeline(positive, [("filter", only_even)])
print("Парні:", even)

squared = apply_pipeline(even, [("map", square)])
print("Квадрат:", squared)