from vehicles import Vehicle

class Yacht(Vehicle):
    def __init__(self, fuel_capacity, fuel_type, name, description, color):
        super().__init__(fuel_capacity, fuel_type, name, description, color)
        self.has_sails = True