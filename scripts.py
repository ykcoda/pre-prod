"""
Polymorphism
Having many forms
"""


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


class Plane(Vehicle):

    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

    def start(self):
        print("Plane is starting")

    def stop(self):
        print("Plane is stopping")


class Car(Vehicle):

    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")


class MotorBike(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def start(self):
        print("MotorBike is starting")

    def stop(self):
        print("MotorBike is stopping")


# Create list of Vehicle to inspect
vehicles: list[Vehicle] = [
    Car("Ford", "Focus", 2012, 4, 4),
    MotorBike("Honda", "Scoopy", 2018),
    Car("Benz", "C Class", 2025, 4, 4),
    Plane("Boeing", "777", 2023, 3, 3),
]


for vehicle in vehicles:
    # print(vehicle.__dict__)
    print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
    vehicle.start()
    vehicle.stop()

# for vehicle in vehicles:
#     if isinstance(vehicle, Vehicle):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()
#     else:
#         raise Exception("Object is not a valid Vehicle")


# Loop through list of vehicles and inspect them
# for vehicle in vehicles:
#     if isinstance(vehicle, Car):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start()
#         vehicle.stop()

#     elif isinstance(vehicle, MotorBike):
#         print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#         vehicle.start_bike()
#         vehicle.stop_bike()
#     else:
#         raise Exception("Object is not a valid Vehicle")
