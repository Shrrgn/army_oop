from generic_item import BaseItem


class DefaultItem(BaseItem):
    health = 0
    defence = 0
    set_type = None
    unit_types = []


class Sword(DefaultItem):
    health = 14
    set_type = "weapon"
    unit_types = ["knight"]


class CoolSword(DefaultItem):
    health = 18
    set_type = "weapon"
    unit_types = ["knight"]


class SoSword(DefaultItem):
    health = 16
    defence = -2
    set_type = "weapon"
    unit_types = ["knight"]


class PowerfulBow(DefaultItem):
    health = 16
    defence = -2
    set_type = "weapon"
    unit_types = ["archer"]
