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


class Car(Vehicle):

    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels


class MotorBike(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def start_bike(self):
        print("Motor Bike is starting")

    def stop_bike(self):
        print("Motor Bike is stoping")
        
# Create list of Vehicle to inspect
vehicles = [Car("Ford", "Focus", 2012, 4, 4), MotorBike("Honda", "Scoopy", 2018), "Jacket"]

# Loop through list of vehicles and inspect them
for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
        
    elif isinstance(vehicle, MotorBike):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start_bike()
        vehicle.stop_bike()
    else: 
        raise Exception("Object is not a valid Vehicle")