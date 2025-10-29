"""
I: Interface Segregation Principle (ISP)

Clients should not be forced to depend on interfaces they do not use.
"""

from abc import ABC, abstractmethod
import math

class Shape2D(ABC):
    @abstractmethod
    def area(self):
        pass


class Shape3D(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def volume(self):
        pass


class Circle(Shape2D):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Shpere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 4 * math.pi * self.radius**2

    def volume(self):
        return (4 / 3) * math.pi(self.radius**3)

