import math
import random
import uuid
from typing import Generic, TypeVar

from abstract_unit import AbstractUnit
from generic_item import GenericItem


GenericUnit = TypeVar('GenericUnit')  # I am not sure that it is correct


def check_if_dead(func):

    def wrapper(self, *args, **kwargs):
        if not self:
            raise Exception(f"Unit {self.__class__.__name__} is dead")

        return func(self, *args, **kwargs)

    return wrapper


# TODO: problem with descriptors
# Currently, don't know how to make it beautiful

class ArmyUnit(AbstractUnit, Generic[GenericUnit]):
    # health_scale
    # hit_number
    # defense_percent
    # critical_hit_percentage
    # critical_hit_percentage_occurrence
    # killing_unit_experience
    # experience_scale

    def __init__(self):
        self._unique_name = f"{self.__class__.__name__.lower()}-{uuid.uuid4().clock_seq}"
        self._unit_name = self.__class__.__name__.lower()

        # is alive
        self._active = True

        # experience
        self._level = 1
        self._experience_now = 0

        # health
        self._health_number = self.health_scale

        self._items_inventory = []
        self._current_set = {
            "weapon": None,
            "armor": None,
            "medallion": None
        }

    @property
    def experience_now(self):
        return self._experience_now

    @property
    def current_set(self):
        return self._current_set

    @property
    def level(self):
        return self._level

    @property
    def defence_percent(self):
        return self._defence_percent

    @defence_percent.setter
    def defence_percent(self, value: int | float):
        if value < 0 or value > 1:
            raise ValueError(
                f"Unit {self.__class__.__name__} should have defence_percent > 0 or < 1"
            )

        self._defence_percent = value

    @property
    def experience_scale(self):
        return self._experience_scale

    @experience_scale.setter
    def experience_scale(self, value: int | float):
        if value <= 0:
            raise ValueError(
                f"Unit {self.__class__.__name__} should have experience_scale > 0"
            )

        self._experience_scale = value

    @property
    def critical_hit_percentage_occurrence(self):
        return self._critical_hit_percentage_occurrence

    @critical_hit_percentage_occurrence.setter
    def critical_hit_percentage_occurrence(self, value: int | float):
        if value <= 0 or value >= 1:
            raise ValueError(
                f"Unit {self.__class__.__name__} should have critical_hit_percentage_occurrence > 0 or < 1"
            )

        self._critical_hit_percentage_occurrence = value

    @property
    def killing_unit_experience(self):
        return self._killing_unit_experience

    @killing_unit_experience.setter
    def killing_unit_experience(self, value: int | float):
        if value <= 0:
            raise ValueError(
                f"Unit {self.__class__.__name__} should have critical_hit_percentage_occurrence > 0"
            )

        self._killing_unit_experience = value

    @property
    def unit_name(self):
        return self._unit_name

    @property
    def unique_name(self):
        return self._unique_name

    @property
    def health_number(self):
        return self._health_number

    @property
    def health_scale(self):
        return self._health_scale

    @health_scale.setter
    def health_scale(self, value: int | float):
        if value < 0:
            raise ValueError("health_scale shoulb be > 0")

        self._health_scale = value

    @property
    def hit_number(self):
        return self._hit_number

    @hit_number.setter
    def hit_number(self, value: int | float):
        if value <= 0:
            raise ValueError(f"Unit {self.__class__.__name__} should have hit_number > 0")

        self._hit_number = value

    @property
    def critical_hit_percentage(self):
        return self._critical_hit_percentage

    @critical_hit_percentage.setter
    def critical_hit_percentage(self, value: int | float):
        if value <= 0 or value >= 1:
            raise ValueError(f"Unit {self.__class__.__name__} should have critical_hit_percentage > 0 or < 1")

        self._critical_hit_percentage = value

    @check_if_dead
    def get_hurt(self, value):
        self._health_number -= int(value)
        print(f"Health number of {self.unique_name} is {self.health_number}")

        if self.health_number <= 0:
            self.die()

    @check_if_dead
    def add_experience(self, other: GenericUnit):
        self._experience_now += other.killing_unit_experience
        print(f"Add {other.killing_unit_experience} experience to {self.unique_name}")

        if self._experience_now >= self.experience_scale:
            self._experience_now = self._experience_now - self.experience_scale
            self.level_up()

    @check_if_dead
    def attack(self, other: GenericUnit):
        critical = (
            self.hit_number * self.critical_hit_percentage
            if random.random() <= self.critical_hit_percentage_occurrence
            else 0
        )
        reduce_health_number = self.hit_number - (self.hit_number * other.defence_percent) - critical
        print(f"{self.unique_name} attack {other.unique_name} with {reduce_health_number} points")
        other.get_hurt(reduce_health_number)

        if not other:
            self.add_experience(other)

    def die(self):
        self._active = False
        print(f"{self.unique_name} is dead now...")

    @check_if_dead
    def level_up(self):
        self._level += 1
        self.experience_scale = (self.experience_scale * math.pi) / 3
        self.health_scale = (self.health_scale * math.pi) / 3
        self._health_number = self.health_scale

        print(f"{self.unique_name} gained a new level. New stats {self.__repr__()}")

    def __bool__(self):
        """
        Returns True if a unit is alive otherwise returns False
        """
        return self._active

    def __repr__(self):
        return f"{self.unique_name}(level={self.level},health_number={self.health_number}," \
               f"hit_number={self.hit_number})"

    @check_if_dead
    def add_item(self, item: GenericItem):
        self._items_inventory.append(item)

    @check_if_dead
    def equip(self):
        for stat in self._current_set:
            try:
                better_item = max(
                    filter(lambda x: stat == x.set_type, self._items_inventory),
                    key=lambda x: x.score
                )
            except ValueError:
                self._current_set[stat] = None
            else:
                self._current_set[stat] = better_item
