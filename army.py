import random
from typing import TypeVar, Generic

from generic_unit import GenericUnit
from units import Knight, Mage, Archer

GenericArmy = TypeVar('GenericArmy')  # I am not sure that it is correct


class Army(Generic[GenericArmy]):
    UNITS = {
        "knight": Knight,
        "mage": Mage,
        "archer": Archer
    }

    def __init__(self, name: str, number: int = 20):
        self.number = number
        self.name = name
        self.stats = {i: 0 for i in self.UNITS.keys()}

        self._create_army()

    def _create_army(self):
        army = []

        for i in range(self.number):
            unit_class = random.choice(list(self.UNITS.keys()))
            army.append(self.UNITS[unit_class]())
            self.stats[unit_class] += 1

        self.army = army

    @classmethod
    def create_specific_army(cls, units_dict: dict[str, GenericUnit]):
        army = []
        for unit_type, unit_number in units_dict.items():
            for i in range(unit_number):
                army.append(cls.UNITS[unit_type])

        cls.army = army
        return cls

    def __bool__(self):
        return len(self.army) != 0

    def __len__(self):
        return len(self.army)

    def _first_move_army(self, other: GenericArmy):
        armies = [self, other]
        who_is_first = random.choice([self, other])
        armies.remove(who_is_first)
        army_1 = who_is_first
        army_2 = armies[0]

        return army_1, army_2

    def fight(self, other: GenericArmy):
        army_1, army_2 = self._first_move_army(other)

        while self and other:
            army_1, army_2 = army_1._fight(army_2)

        print(f"Army {self.name if self else other.name} won")
        print(f"{self.name} => {len(self)}; {other.name} => {len(other)}")

    def _fight(self, other: GenericArmy):
        unit = random.choice(self.army)
        other_unit = random.choice(other.army)

        unit.attack(other_unit)

        if not other_unit:
            print(f"{other_unit} dies")
            other.army.remove(other_unit)
            print(f"{other.name} is now only {len(other)}")

        return other, self


a = Army("blue", number=1000)
b = Army("red", number=1000)
a.fight(b)
print(a.stats)
print(b.stats)
# print(a.create_army())
