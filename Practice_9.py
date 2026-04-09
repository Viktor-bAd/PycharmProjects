from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(
        self,
        name: str,
        max_hp: int,
        level: int,
        intelligence: int,
        strength: int,
        dexterity: int,
        mana: int,
        defense: int
    ):
        self.name: str = name
        self._max_hp: int = max_hp
        self._hp: int = max_hp
        self.level: int = level
        self._intelligence: int = intelligence
        self._strength: int = strength
        self._dexterity: int = dexterity
        self._mana: int = mana
        self._defense: int = defense

    @abstractmethod
    def attack(self: int):
        pass

    def take_damage(self: int, damage: int):
        real_damage = damage - self._defense
        if real_damage < 0:
            real_damage = 0
        self._hp -= real_damage
        if self._hp < 0:
            self._hp = 0
        return real_damage

    def level_up(self: int):
        if self.level < 20:
            self.level += 1
        return self.level

    def increase_stat(self, stat: str):
        stats = {
            "intelligence": self._intelligence,
            "strength": self._strength,
            "dexterity": self._dexterity,
            "mana": self._mana,
            "defense": self._defense
        }

        if stat in stats:
            new_value = stats[stat] + 1

            if stat == "intelligence":
                self._intelligence = new_value
            elif stat == "strength":
                self._strength = new_value
            elif stat == "dexterity":
                self._dexterity = new_value
            elif stat == "mana":
                self._mana = new_value
            elif stat == "defense":
                self._defense = new_value

            return new_value
        return -1

    def rest(self) -> int:
        self._hp = self._max_hp
        return self._hp

    def heal(self, heal_hp: int) -> int:
        self._hp += heal_hp
        if self._hp > self._max_hp:
            self._hp = self._max_hp
        return self._hp


class Paladin(Character):
    def attack(self: int):
        if self._mana >= 5:
            self._mana -= 5
            return 4 * self._strength
        return self._strength

    def shield(self: int):
        bonus = 4 + self.level
        self._defense += bonus
        return self._defense

    def unshield(self: int):
        penalty = 4 + self.level
        self._defense -= penalty
        if self._defense < 0:
            self._defense = 0
        return self._defense

    def heal_ally(self, ally: Character):
        heal_amount = int(5 + 2 * self.level + 0.5 * self._mana)
        ally.heal(heal_amount)
        return heal_amount


class Mage(Character):
    def attack(self) -> int:
        if self._mana >= 3:
            self._mana -= 3
            return 3 * self._intelligence + 4
        return 0

    def fireball(self) -> int:
        if self._mana >= 5:
            self._mana -= 5
            return 2 * self._intelligence + 3
        return 0

    def heal_ally(self, ally: Character) -> int:
        heal_amount = 3 + self.level + 3 * self._intelligence
        ally.heal(heal_amount)
        return heal_amount
