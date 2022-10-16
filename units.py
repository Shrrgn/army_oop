from generic_unit import Unit


class DefaultUnit(Unit):
    health_scale = 100
    hit_number = 10
    defence_percent = 0.05
    critical_hit_percentage = 0.05
    critical_hit_percentage_occurrence = 0.01
    killing_unit_experience = 10
    experience_scale = 100


class Knight(DefaultUnit):
    health_scale = 120
    defence_percent = 0.1
    hit_number = 10


class Archer(DefaultUnit):
    health_scale = 90
    hit_number = 12
    critical_hit_percentage = 0.1


class Mage(DefaultUnit):
    health_scale = 70
    defence_percent = 0.01
    hit_number = 130
