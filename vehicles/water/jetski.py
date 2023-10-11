from vehicles import Vehicle, WaterBorne
from fuels import Gasoline

class JetSki(Vehicle, WaterBorne): # Mixin strategy (goal of composition)
    def __init__(self, fuel_capacity, name, description, color):
        Vehicle.__init__(self, fuel_capacity, name, description, color)
        WaterBorne.__init__(self)

        # Composition strategy (goal of composition)
        # Type of Association
        self.fuel_type = Gasoline("medium")
