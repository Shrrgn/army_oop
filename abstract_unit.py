
from abc import ABC, abstractmethod


class AbstractUnit(ABC):

    @abstractmethod
    def attack(self, other):
        pass

    @abstractmethod
    def die(self):
        pass

    @abstractmethod
    def level_up(self):
        pass

    @abstractmethod
    def get_hurt(self, value):
        pass

    @property
    @abstractmethod
    def health_number(self):
        pass

    @property
    @abstractmethod
    def hit_number(self):
        pass

    @property
    @abstractmethod
    def critical_hit_percentage(self):
        pass

    @property
    @abstractmethod
    def critical_hit_percentage_occurrence(self):
        pass

    @property
    @abstractmethod
    def killing_unit_experience(self):
        pass

    @property
    @abstractmethod
    def experience_scale(self):
        pass

    @property
    @abstractmethod
    def defence_percent(self):
        pass
