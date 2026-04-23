from abc import ABC, abstractmethod

class Pet(ABC):
    def __init__(self, name, satiety=50, energy=50):
        self._name = name
        self._satiety = max(0, min(100, satiety))
        self._energy = max(0, min(100, energy))

    def sleep(self):
        self._energy = 100
        print(f"{self._name} відпочив(ла) і тепер має 100 енергії.")

    def eat(self, food_amount):
        self._satiety = min(100, self._satiety + food_amount)
        print(f"{self._name} поїв(ла). Ситість: {self._satiety}")

    @abstractmethod
    def play(self, activity_level):
        pass

    def make_sound(self):
        pass


# --- Cat ---
class Cat(Pet):
    def play(self, activity_level):
        if self._satiety > 60:
            self._energy = max(0, self._energy - 2 * activity_level)
            self._satiety = max(0, self._satiety - activity_level)
            print(f"{self._name} грається. Енергія: {self._energy}, Ситість: {self._satiety}")
        else:
            print(f"{self._name} занадто голодний(а) для гри.")

    def make_sound(self):
        print("Мяу")

    def catch_mouse(self):
        if self._energy > 30:
            if self._satiety > 40:
                print(f"{self._name} впіймав(ла) мишу і грається з нею.")
            else:
                self._satiety = min(100, self._satiety + 20)
                print(f"{self._name} впіймав(ла) мишу і з'їв(ла) її. Ситість: {self._satiety}")
        else:
            print(f"{self._name} занадто втомлений(а), щоб ловити мишу.")


# --- Dog ---
class Dog(Pet):
    def play(self, activity_level):
        if self._satiety > 15:
            loss = activity_level // 2
            self._energy = max(0, self._energy - loss)
            self._satiety = max(0, self._satiety - loss)
            print(f"{self._name} грається. Енергія: {self._energy}, Ситість: {self._satiety}")
        else:
            print(f"{self._name} занадто голодний(а) для гри.")

    def make_sound(self):
        print("Гав")

    def fetch_ball(self):
        if self._satiety > 10:
            self._energy = max(0, self._energy - 5)
            print(f"{self._name} приніс(ла) м'яч. Енергія: {self._energy}")
        else:
            print(f"{self._name} не хоче бігти за м'ячем — голодний(а).")



cat = Cat("Мурка")
dog = Dog("Бобік")

cat.make_sound()
cat.play(10)
cat.catch_mouse()

print()

dog.make_sound()
dog.play(10)
dog.fetch_ball()
