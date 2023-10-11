from .fuel import Fuel

class Propellant(Fuel):
    def __init__(self, chemical:str, solid:bool) -> None:
        super().__init__(chemical, 10000, "kilogram")
        self.solid = solid
