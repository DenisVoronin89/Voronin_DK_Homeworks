"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception): # declare LowFuelError exception
    pass


class NotEnoughFuel(Exception): # declare NotEnoughFuel exception
    pass


class CargoOverload(Exception): # declare CargoOverLoad exception
    pass
