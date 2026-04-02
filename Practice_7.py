
import math


class Rectangle:
    def __init__(self, width:float, height:float):
        self._width = width
        self._height = height

    def get_perimeter(self)->float:
        return 2 * (self._width + self._height)

    def display_info(self):
        print(f"Rectangle width: {self._width}, height: {self._height}")


class Circle:
    def __init__(self, radius:float):
        self._radius = radius

    def get_perimeter(self)->float:
        return 2 * math.pi * self._radius

    def display_info(self):
        print(f"Circle radius: {self._radius}")


class Triangle:
    def __init__(self, sideA:float, sideB:float, sideC:float):
        self._sideA = sideA
        self._sideB = sideB
        self._sideC = sideC

    def get_perimeter(self)->float:
        return self._sideA + self._sideB + self._sideC

    def display_info(self):
        print(f"Triangle: {self._sideA}, {self._sideB}, {self._sideC}")


def create_figure()-> Rectangle | Circle | Triangle | None:
    figure_type= input("Enter figure type Rectangle, Circle, Triangle: ")

    if figure_type == "Rectangle":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        return Rectangle(width, height)

    elif figure_type == "Circle":
        radius = float(input("Enter radius: "))
        return Circle(radius)

    elif figure_type == "Triangle":
        sideA = float(input("Enter side A: "))
        sideB = float(input("Enter side B: "))
        sideC = float(input("Enter side C: "))
        return Triangle(sideA, sideB, sideC)

    else:
        print("Invalid figure_type")
        return None


figures = []
figures.append(create_figure())
figures.append(create_figure())
figures.append(create_figure())

for figure in figures:
    if figure != None:
        figure.display_info()
        print(figure.get_perimeter())



class Manager:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary

    def display_info(self):
        print(f"Manager: {self.name}, salary={self.get_salary()}")


class Developer:
    def __init__(self, name, base_salary, work_experience):
        self.name = name
        self.base_salary = base_salary
        self.work_experience = work_experience

    def get_salary(self):
        if self.work_experience > 4:
            return self.base_salary * 1.2
        return self.base_salary

    def display_info(self):
        print(f"Developer: {self.name}, experience={self.work_experience} years, salary={self.get_salary():.2f}")


class Intern:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary / 2

    def display_info(self):
        print(f"Intern: {self.name}, salary={self.get_salary():.2f}")


def create_worker():
    worker_type = input("Введіть тип працівника (manager/developer/intern): ").lower()

    name = input("Введіть ім'я: ")
    base_salary = float(input("Введіть базову ставку: "))

    if worker_type == "manager":
        return Manager(name, base_salary)
    elif worker_type == "developer":
        work_experience = int(input("Введіть стаж роботи в роках: "))
        return Developer(name, base_salary, work_experience)
    elif worker_type == "intern":
        return Intern(name, base_salary)
    else:
        print("Невідомий тип працівника.")
        return None


workers = [
    Manager("Alice", 1000),
    Developer("Bob", 1200, 5),
    Intern("Charlie", 800)
]


for worker in workers:
    worker.display_info()



class Car:
    def __init__(self, speed):
        self.check_speed(speed)
        self.speed = speed

    def check_speed(self, speed):
        if not (20 <= speed <= 200):
            raise ValueError(f"Неправильна швидкість для Car: {speed}. Має бути від 20 до 200 км/год.")

    def move(self):
        print(f"Car їде по шосе зі швидкістю {self.speed} км/год.")


class Bicycle:
    def __init__(self, speed):
        self.check_speed(speed)
        self.speed = speed

    def check_speed(self, speed):
        if not (10 <= speed <= 30):
            raise ValueError(f"Неправильна швидкість для Bicycle: {speed}. Має бути від 10 до 30 км/год.")

    def move(self):
        print(f"Bicycle їде по дорозі зі швидкістю {self.speed} км/год.")


class Boat:
    def __init__(self, speed):
        self.check_speed(speed)
        self.speed = speed

    def check_speed(self, speed):
        if not (0 <= speed <= 50):
            raise ValueError(f"Неправильна швидкість для Boat: {speed}. Має бути від 0 до 50 км/год.")

    def move(self):
        print(f"Boat пливе по воді зі швидкістю {self.speed} км/год.")


def create_vehicle():
    vehicle_type = input("Введіть тип транспорту (car/bicycle/boat): ").lower()
    speed = float(input("Введіть швидкість: "))

    try:
        if vehicle_type == "car":
            return Car(speed)
        elif vehicle_type == "bicycle":
            return Bicycle(speed)
        elif vehicle_type == "boat":
            return Boat(speed)
        else:
            print("Невідомий тип транспорту.")
            return None
    except ValueError as ve:
        print("Помилка:", ve)
        return None



vehicles = [
    Car(100),
    Bicycle(25),
    Boat(30)
]
