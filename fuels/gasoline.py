from .fuel import Fuel

class Gasoline(Fuel):
    def __init__(self, grade) -> None:
        super().__init__("Petroleum Gasoline", 3.5, "gallon")
        self.grade = grade
