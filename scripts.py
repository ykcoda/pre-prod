"""
D: Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should
depend pn abstractions.
"""

from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class BasicEngine(Engine):
    def start(self):
        print("Basic Engine Started")


class FastEngine(Engine):
    def start(self):
        print("Fast Engine Started")


class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()
        print("Car Started")


car = Car(BasicEngine())
car.start()
