from typing import TypeVar, Generic

from abstract_item import AbstractItem

GenericItem = TypeVar('GenericItem')  # I am not sure that it is correct


class BaseItem(AbstractItem, Generic[GenericItem]):

    def __init__(self):
        self._name = self.__class__.__name__

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
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = value

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
        item_stats = ["health", "defence"]

        return sum([getattr(self, stat) for stat in item_stats]) / len(item_stats)

    @property
    def score(self):
        return self._calculate_item_score()

    def __eq__(self, other: GenericItem):
        return self.set_type == other.set_type and self.score == other.score

    def __gt__(self, other: GenericItem):
        return self.set_type == other.set_type and self.score > other.score
