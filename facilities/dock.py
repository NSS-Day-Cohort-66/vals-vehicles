from .facility import Facility

class Dock(Facility):
    def __init__(self, name, location, vehicle_capacity, base_cost, depth_min, depth_max) -> None:
        super().__init__(name, location, vehicle_capacity, base_cost)

        self.depth_min = depth_min
        self.depth_max = depth_max


    def add_vehicle(self, vehicle):
        try:
            if vehicle.has_sails:
                self.vehicles.append(vehicle)
                print(f'{vehicle.name} has been added to {self.name}')
        except AttributeError:
            print("You can only add water craft to a dock")
