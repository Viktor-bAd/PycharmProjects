class Passenger:
    def __init__(self, name, destination):
        self._name = name
        self._destination = destination


class Transport:
    def __init__(self, speed):
        self._speed = speed

    def move(self, destination, distance):
        time = distance / self._speed
        print(f"Транспорт прибув до {destination}.")
        print(f"Час у дорозі: {time:.2f} год.")


class Bus(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed)
        self._capacity = capacity
        self._passengers = []

    def board_passenger(self, passenger):
        if len(self._passengers) < self._capacity:
            self._passengers.append(passenger)
            print(f"{passenger._name} сів у автобус.")
        else:
            print("В автобусі немає місць.")

    def move(self, destination, distance):
        count = 0
        remaining = []

        for passenger in self._passengers:
            if passenger._destination == destination:
                count += 1
            else:
                remaining.append(passenger)

        self._passengers = remaining

        print(f"На зупинці {destination} вийшло пасажирів: {count}")

        super().move(destination, distance)



p1 = Passenger("Іван", "Київ")
p2 = Passenger("Олена", "Львів")
p3 = Passenger("Максим", "Київ")

bus = Bus(60, 2)

bus.board_passenger(p1)
bus.board_passenger(p2)
bus.board_passenger(p3)

bus.move("Київ", 120)
