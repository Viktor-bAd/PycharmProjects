from abc import ABC, abstractmethod
from enum import Enum


class Robot(ABC):
    def __init__(self, name, battery_level=100):
        self.name = name
        self.battery_level = battery_level
        self.status = "off"

    def info(self):
        print(f"Name: {self.name}")
        print(f"Battery level: {self.battery_level}%")
        print(f"Status: {self.status}")

    def charge(self):
        self.battery_level = 100
        print(f"{self.name} fully charged.")

    def turn_on(self):
        self.status = "on"
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.status = "off"
        print(f"{self.name} is now OFF.")


class CleaningMode(Enum):
    dry = "dry"
    wet = "wet"


class CleaningRobot(Robot):
    def __init__(
            self,
            cleaning_mode: CleaningMode,
            name: str,
            battery_level: int =100,
            dust_level: int=0,
            water_level: int=100,
    ):
        super().__init__(name, battery_level)
        self._cleaning_mode = cleaning_mode
        self._dust_level = dust_level
        self._water_level = water_level

    def info(self):
        super().info()
        print(f"Cleaning mode: {self._cleaning_mode.name}")
        print(f"Dust level: {self._dust_level}")
        print(f"Water level: {self._water_level}")

    def turn_on(self):
        if self._dust_level == 100:
            print(f"{self.name} Container is full")
            return

        if self._water_level == 0 and self._cleaning_mode == CleaningMode.wet:
            print(f"{self.name} Water is Empty")
            return

        super().turn_on()

    def empty_dustbin(self):
        self._dust_level = 0
        print(f"{self.name} dust bin is empty")

    def fill_water(self):
        self._water_level = 100
        print(f"{self.name} fill water is Full")

    def swap_mode(self):
        if self._cleaning_mode == CleaningMode.dry:
            self._cleaning_mode = CleaningMode.wet
        else:
            self._cleaning_mode = CleaningMode.dry
        print(f"{self.name} swapped mode is {self._cleaning_mode.name}")

    def clean(self, energy:int, dust:int, water=None):
        if self.status == "off":
            print(f"{self.name} Cleaning is off")
            return

        if water is None and self._cleaning_mode == CleaningMode.wet:
            print(f"{self.name} Cleaning is off")
            return

        if self._cleaning_mode == CleaningMode.wet and self._water_level < water:
            print(f"{self.name} Cleaning is off")
            return

        if self._dust_level + dust > 100:
            print(f"{self.name} Cleaning is off")
            return

        if self.battery_level < energy:
            print(f"{self.name} Cleaning is off")
            return

        self._dust_level += dust
        if self._cleaning_mode == CleaningMode.wet:
            self._water_level -= water
        self.battery_level -= energy


class SecurityRobot(Robot):
    def __init__(
            self,
            name: str,
            min_speed: int,
            alert_level,
            dengerous_items: list[str] = None,
            battery_level: int = 100,
            status: str="off",
    ):
        super().__init__(name, battery_level)

        self._alert_level = alert_level
