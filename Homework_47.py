# Завдання 1

class Cart:
    def __init__(self, client):
        self.client = client
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Товар не знайдено в кошику")

    def show_info(self):
        print(f"Клієнт: {self.client}")
        print("Товари:", ", ".join(self.items) if self.items else "кошик порожній")


cart = Cart("Іван")

cart.add_item("яблуко")
cart.add_item("хліб")
cart.show_info()

cart.remove_item("яблуко")
cart.show_info()


# Завдання 2

class Phone:
    def __init__(self, number, battery_level):
        self.number = number
        self.battery_level = battery_level

    def use_battery(self, percent):
        self.battery_level -= percent

        if self.battery_level < 0:
            self.battery_level = 0

        if self.battery_level < 20:
            print("Заряд низький!")

    def show_info(self):
        print(f"Номер: {self.number}, Заряд: {self.battery_level}%")


phone = Phone("+380123456789", 50)

phone.show_info()
phone.use_battery(35)
phone.show_info()
