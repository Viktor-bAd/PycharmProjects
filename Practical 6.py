class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def show_info(self):

        print(f"Ім’я: {self.name}, вік: {self.age}")


student1 = Student("Іван", 20)
student2 = Student("Вікор", 25)
student3 = Student("Ігор", 30)

students = []
students.append(student1)
students.append(student2)
students.append(student3)

for student in students:
    student.show_info()




# Створіть клас Circle з атрибутом radius. Додайте метод для
# отримання площі кола

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

circle = Circle(5)
circle2 = Circle(10)
print("Площа кола:",circle.get_area())
print("Площа кола:",circle2.get_area())


# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатньо коштів!")
        else:
            self.balance -= amount

    def info(self):
        print(f"Власник: {self.owner}, Баланс: {self.balance}")


acc = BankAccount("Іван", 1000)

acc.info()
acc.deposit(200)
acc.withdraw(500)
acc.info()


# Створіть клас Car з атрибутами brand(марка), year(рік випуску), is_ready(чи готовий до поїздки, за замовчування False).
# Додайте метод start_engine який заводить двигун, і змінює атрибут is_ready
# Додайте метод move який виводить повідомлення, що автомобіль їде, або ж ще не готовий в залежності від is_ready.


class Car:
    def __init__(self, brand, year, is_ready=False):
        self.brand = brand
        self.year = year
        self.is_ready = is_ready

    def start_engine(self):
        self.is_ready = True
        print("Двигун запущено")

    def move(self):
        if self.is_ready:
            print(f"{self.brand} їде")
        else:
            print(f"{self.brand} ще не готовий до поїздки")


car = Car("BMW", 2020)

car.move()
car.start_engine()
car.move()
