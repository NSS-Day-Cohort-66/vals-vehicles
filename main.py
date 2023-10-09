# import all package members here
from vehicles.water import JetSki, Yacht
from vehicles.air import Airplane
from vehicles.space import HeavyRocket
from facilities.hangar import Hangar
from facilities import Dock

# Vehicle Class Property Key (fuel_capacity, fuel_type, name, description, color)

# Specific types of vehicles
sea_doo = JetSki(8, "Gas", "Sea-Doo RXP-X 325", "Super fun", "Neon Blue")
sea_doo.total_distance_traveled = 10
print(f"My {sea_doo.color} {sea_doo.name} is {sea_doo.description} and has traveled {sea_doo.total_distance_traveled}")



# HeavyRockets property key(fuel_capacity, fuel_type, name, description, color, number_of_thrusters, payload, payload_weight)
falcon_heavy = HeavyRocket(
    200000,
    "Rocket Fuel",
    "SpaceX Falcon Heavy Rocket",
    "It's not light",
    "White",
    27,
    "Satellite",
    2500,
)
print(f"{falcon_heavy.name} is {falcon_heavy.description}")

# airplane (self, fuel_capacity, fuel_type, name, description, color, wing_span, max_altitude)
boeing_747 = Airplane(
    20000,
    "Jet Fuel",
    "Boeing 747",
    "a large commercial airplane",
    "White",
    64.44,
    35000,
)
print(f"{boeing_747.name} is {boeing_747.description}")

# yacht
open_yacht = Yacht(10000, "E10", "Open Yacht", "open deck for warm seas", "white")
print(f"My {open_yacht.color} {open_yacht.name} has an {open_yacht.description}")

# tampa_airport = Hangar("Tampa International Airport")

# tampa_airport.add_vehicle(boeing_747)




los_angeles = Dock("Los Angeles", "Los Angeles", 700, 2, 4, 10)
los_angeles.add_vehicle(boeing_747)
los_angeles.add_vehicle(sea_doo)
for vehicle in los_angeles.vehicles:
    print(vehicle)


# 1. Make classes for each vehicle
# 2. Make a generic class for "Vehicle" that other can inherit from
# 3. Define all appropriate properties for the required data
# 4. Method for making trips
# 5. Method for refueling
# 6. Method for tracking total kilometers traveled
# 7. Method/property for where vehicle is stored
# 8. Track if vehicle is currently traveling
# 9. Method for adding a vehicle to the total catalog/inventory for Val
# 10. Think about the different kinds of vehicle to categorize them
# 11. Update catalog when vehicle is no longer in use
# 12. We'll need the datetime package
# 13. Package for land vehicles
# 14. Package for water vehicles
# 15. Package for air vehicles
# 16. Package or space vehicles
# 17. Base vehicles package that contains all above
# 18. Base package for facilities (where they will be refueled)
# 19. Property for fuel type
# 20. Property for storage cost on facility
# 21. Property for fuel price on facility or vehicle????????
# 22. Base package for fuels
