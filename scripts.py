"""
D: Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should
depend pn abstractions.
"""


class Engine:
    def start(self):
        print("Engine Started.")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Car Started")
        
car = Car()
car.start()