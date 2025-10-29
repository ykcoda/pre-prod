"""
Composition
This involves creating complex objects by combining simpler object or components.
"""

"""
Composition vrs Inheritance


Composition: 
1. When you need more flexibity in constructing objects by assembling smalle, reusable components
2. When there is no clear "is-a" relationship between classes and a "has-a" relationship is more appropriate
3. When you want to avaoid the limitation of inheritance, such as tight coupling and the frigile base class problem

Inheritance:
1. When there is a clear "is-a" relationship between classes and subclasses objects can be treated as instances of their superclass.
2. When you want to promote code reuse by inheriting properties and behaviours from existing classes
"""


class Engine:

    def start(self):
        print("Engine starting")


class Wheels:
    def rotates(self):
        print("Rotate wheels")


class Chassis:
    def support(self):
        print("Chassis is supporting car")


class Seat:
    def sit(self):
        print("Sitting on seats")


class Car:
    def __init__(self):
        self._engine = Engine()
        self._wheels = Wheels()
        self._chassis = Chassis()
        self._seat = Seat()

    def start(self):
        self._engine.start()
        self._wheels.rotates()
        self._chassis.support()
        self._seat.sit()


car1 = Car()
car1.start()
