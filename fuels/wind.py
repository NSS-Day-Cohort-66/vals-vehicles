from .fuel import Fuel

class Wind(Fuel):
    def __init__(self) -> None:
        super().__init__("Wind", 0, "")
