from enum import Enum, unique


@unique
class UnitItemsSet(Enum):
    WEAPON = "weapon"
    ARMOR = "armor"
    MEDALLION = "medallion"


@unique
class ItemStats(Enum):
    HIT_NUMBER = "hit_number"
    DEFENCE = "defence"


def check_if_dead(func):

    def wrapper(self, *args, **kwargs):
        if not self:
            raise Exception(f"Unit {self.__class__.__name__} is dead")

        return func(self, *args, **kwargs)

    return wrapper


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]
