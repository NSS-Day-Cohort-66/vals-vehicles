class Garage():
    def __init__(self, flooring, levels) -> object:
        self.flooring = flooring
        self.levels = levels
        self.vehicles = []

    def park(self, vehicle) -> None:
        self.vehicles.append(vehicle)
