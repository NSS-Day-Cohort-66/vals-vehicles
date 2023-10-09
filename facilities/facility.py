class Facility:
    def __init__(self, name, location, vehicle_capacity, base_cost) -> None:
        self.name = name
        self.location = location
        self.vehicle_capacity = vehicle_capacity
        self.base_cost = base_cost
        self.vehicles = set()


    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f'{vehicle.name} has been added to {self.name}')


    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)