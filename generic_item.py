from typing import TypeVar, Generic

from abstract_item import AbstractItem
from utils import ItemStats

GenericItem = TypeVar('GenericItem')  # I am not sure that it is correct


class Item(AbstractItem, Generic[GenericItem]):

    def __init__(
            self,
            name: str,
            set_type: str,
            unit_types: list[str],
            hit_number: int | float = 0,
            defence: int | float = 0,
    ):
        self._name = name
        self.hit_number = hit_number
        self.defence = defence
        self.set_type = set_type
        self.unit_types = unit_types

    # getters and setters
    @property
    def set_type(self):
        return self._set_type

    @set_type.setter
    def set_type(self, value):
        self._set_type = value

    @property
    def unit_types(self):
        return self._unit_types

    @unit_types.setter
    def unit_types(self, value):
        self._unit_types = value

    @property
    def hit_number(self):
        return self._hit_number

    @hit_number.setter
    def hit_number(self, value):
        self._hit_number = value

    @property
    def defence(self):
        return self._defence

    @defence.setter
    def defence(self, value):
        self._defence = value

    @property
    def name(self):
        return self._name

    def _calculate_item_score(self):
        """
        Calculates the item score that is base on stats (private method)
        """
        return sum([getattr(self, stat) for stat in ItemStats.values()]) / len(ItemStats.values())

    @property
    def score(self):
        """
        Calculates the item score that is base on stats
        """
        return self._calculate_item_score()

    def __eq__(self, other: GenericItem):
        """
        Checks if two items are equal by stats
        """
        return self.set_type == other.set_type and self.score == other.score

    def __gt__(self, other: GenericItem):
        """
        Checks if one item is better than another
        """
        return self.set_type == other.set_type and self.score > other.score

    def __repr__(self):
        return f"{self.name}"

    def __hash__(self):
        return hash(f"{self.name}")
