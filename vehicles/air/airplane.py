from vehicles import Vehicle


class Airplane(Vehicle):
    def __init__(
        self,
        fuel_capacity,
        fuel_type,
        name,
        description,
        color,
        wing_span,
        max_altitude,
    ):
        super().__init__(fuel_capacity, fuel_type, name, description, color)
        self.wing_span = wing_span
        self.max_altitude = max_altitude
