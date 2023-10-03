from AirBased import AirBased
from EnginePowered import EnginePowered

# Specific types of vehicles
class Jet(AirBased, EnginePowered):
    def __init__(self):
        AirBased.__init__(self, 150, 20000)
        EnginePowered.__init__(self, "Jet", 5000, "Combustion")

