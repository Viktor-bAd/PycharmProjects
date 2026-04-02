import random

class Car:
    def __init__(self, brand, mileage, fuel_level, fuel_consumption, is_working=True):
        self.brand = brand
        self.mileage = mileage
        self.fuel_level = fuel_level
        self.fuel_consumption = fuel_consumption
        self.is_working = is_working

    def drive(self, distance):
        if not self.is_working:
            print(f"{self.brand} не справний і не може їхати.")
            return

        required_fuel = distance * self.fuel_consumption
        if required_fuel > self.fuel_level:
            print(f"{self.brand} не має достатньо пального для поїздки {distance} км.")
            return

        self.fuel_level -= required_fuel
        self.mileage += distance
        print(f"{self.brand} проїхав {distance} км. Пробіг: {self.mileage} км, Пального: {self.fuel_level:.2f} л.")

        if random.random() < 0.4:
            self.is_working = False
            print(f"{self.brand} зламався під час поїздки!")

    def repair(self):
        if self.is_working:
            print(f"{self.brand} вже справний.")
        else:
            self.is_working = True
            print(f"{self.brand} відремонтовано!")

    def refuel(self, amount):
        if amount <= 0:
            print("Кількість пального повинна бути додатньою.")
            return
        self.fuel_level += amount
        print(f"{self.brand} заправлено {amount} л. Поточний рівень пального: {self.fuel_level:.2f} л.")



my_car = Car("Toyota", 50000, 20, 0.08)  # 0.08 л/км
my_car.drive(100)
my_car.refuel(10)
my_car.repair()
