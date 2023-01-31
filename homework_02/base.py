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
        return


    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Error - Low fuel")



    def move(self, distance):
        quantity = distance // self.fuel_consumption   # check the amount of fuel to overcome a given distance
        if self.fuel > 0 and quantity <= self.fuel:
            self.fuel -= quantity
        else:
            raise NotEnoughFuel("Error - Not enough fuel")





