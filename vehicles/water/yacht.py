from vehicles import Vehicle
from fuels import Wind

class Yacht(Vehicle):
    def __init__(self, fuel_capacity, fuel_type, name, description, color):
        super().__init__(fuel_capacity, fuel_type, name, description, color)
        self.has_sails = True
        self.fuel_type = Wind()