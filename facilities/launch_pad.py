from .facility import Facility

class LaunchPad(Facility):
    def __init__(self, name, location, vehicle_capacity, base_cost, max_load):
        super().__init__(name, location, vehicle_capacity, base_cost)

        self.max_load = max_load