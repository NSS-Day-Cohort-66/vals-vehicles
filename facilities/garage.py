from .facility import Facility

class Garage(Facility):
    def __init__(self,name, location, vehicle_capacity, base_cost, max_height):
        super().__init__(name, location, vehicle_capacity, base_cost)

        self.max_height = max_height

