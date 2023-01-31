"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo: int

    def __init__(self, max_cargo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_cargo = max_cargo


    def load_cargo(self, add_cargo: int, *args, **kwargs):  # check the max load capacity
        new_cargo = self.cargo + add_cargo
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise CargoOverload("Error - Cargo overload")

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo