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
