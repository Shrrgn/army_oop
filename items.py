import random

from generic_item import Item
from utils import ItemStats

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


def generate_items(number: int = 10):
    weapons_list = []
    for i in range(number):
        unit_type = random.choice(list(UNIT_WEAPONS.keys()))
        weapon = random.choice(list(UNIT_WEAPONS[unit_type]))
        item_condition = random.choice(list(ITEM_CONDITIONS.keys()))
        item = Item(
            name=f"{item_condition} {weapon}",
            set_type="weapon",
            unit_types=[unit_type],
            hit_number=DEFAULT_ITEM_STATS["hit_number"] + ITEM_CONDITIONS[item_condition]
        )
        weapons_list.append(item)

    return set(weapons_list)

print(generate_items())
