import random

from generic_item import Item
from utils import ItemStats, SingletonMeta, UnitItemsSet

KNIGHT_WEAPON = ["Sword", "Dagger", "Katana", "Sickle", "Hammer"]
ARCHER_WEAPON = ["Bow"]
MAGE_WEAPON = ["Stick", "Staff"]

UNIT_WEAPONS = {
    "knight": KNIGHT_WEAPON,
    "archer": ARCHER_WEAPON,
    "mage": MAGE_WEAPON
}

DEFAULT_ITEM_STATS = {
    ItemStats.HIT_NUMBER: 8,
    ItemStats.DEFENCE: 8
}

ITEM_CONDITIONS = {
    "Normal": 3,
    "Good": 6,
    "Excellent": 10,
    "New": 12,
    # "Super": 15,
    # "Super-Duper": 20,

    "Bad": -3,
    "Used": -5,
    "Blunt": -10,
    # "Broken": -16,
    # "Cursed": -20,
}


class ItemGenerator(metaclass=SingletonMeta):
    # TODO: change to make it work with defence_percentage
    # TODO: generate items with a few different stats
    def __init__(self, weapons_number: int):
        self._weapons_number = weapons_number
        self._items_inventory = []

    @property
    def inventory(self) -> list[Item]:
        return self._items_inventory

    def _generate_weapons(self):
        """
        Generates weapons based on unit types and a condition of an item
        """
        weapons_list = []

        for i in range(self._weapons_number):
            unit_type = random.choice(list(UNIT_WEAPONS.keys()))
            weapon = random.choice(list(UNIT_WEAPONS[unit_type]))
            item_condition = random.choice(list(ITEM_CONDITIONS.keys()))

            item = Item(
                name=f"{item_condition} {weapon}",
                set_type=UnitItemsSet.WEAPON.value,
                unit_types=[unit_type],
            )
            setattr(
                item,
                ItemStats.HIT_NUMBER.value,
                DEFAULT_ITEM_STATS[ItemStats.HIT_NUMBER.value] + ITEM_CONDITIONS[item_condition]
            )
            weapons_list.append(item)

        self._items_inventory.extend(list(set(weapons_list)))

    def generate_items(self):
        """
        Generates items of different types
        """
        self._generate_weapons()

    def clear(self):
        """
        Clears inventory list
        """
        self._items_inventory = []
