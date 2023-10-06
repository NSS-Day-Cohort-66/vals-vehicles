from vehicles import Vehicle

class HeavyRocket(Vehicle):
    def __init__(self, fuel_capacity, fuel_type, name, description, color, number_of_thrusters, payload, payload_weight):
        super().__init__(fuel_capacity, fuel_type, name, description, color)
        self.number_of_thrusters = number_of_thrusters
        self.payload = payload
        self.payload_weight = payload_weight