class Dock():
    def __init__(self, underwater, material):
        self.underwater = underwater
        self.material = material
        self.vehicles = []

    def dock(self, vehicle):
        self.vehicles.append(vehicle)