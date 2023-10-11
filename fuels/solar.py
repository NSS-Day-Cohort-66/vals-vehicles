from .fuel import Fuel

class Solar(Fuel):
    def __init__(self, panels) -> None:
        super().__init__("Solar Power", 0.10, "kWh")
        self.panel_count = panels