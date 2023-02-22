from abc import ABC


from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    weight: int
    fuel: int
    fuel_consumption: float
    started = False


    def __init__(self, weight, fuel, fuel_consuption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consuption


    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Error - Low fuel")


    def move(self, distance):
           amount_of_fuel = self.fuel_consumption * distance # check the amount of fuel to overcome a given distance
           if self.fuel >= amount_of_fuel:
               self.fuel -= amount_of_fuel
           else:
               raise NotEnoughFuel("Error - Not enough fuel")


