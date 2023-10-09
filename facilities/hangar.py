from .facility import Facility

class Hangar(Facility):

    def __init__(self, name, location, vehicle_capacity, base_cost, wingspan):
        super().__init__(name, location, vehicle_capacity, base_cost)

        self.wingspan = wingspan