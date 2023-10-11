class Vehicle:
    def __init__(self, fuel_capacity, name, description, color):
        self.fuel_capacity = fuel_capacity
        self.name = name
        self.description = description
        self.color = color


    @property
    def total_distance_traveled(self):
        return f"{self.__total_distance_traveled} km"

    @total_distance_traveled.setter
    def total_distance_traveled(self, value):
        if value >= 0:
            self.__total_distance_traveled = value
        else:
            raise TypeError("You must provide a 0, or larger, numeric value")
