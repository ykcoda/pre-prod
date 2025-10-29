"""
L: Listov Substitution Principle (LSP)

Object of a superclass should be replacable with objects of its subclass without affecting the correctness
of the program
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, height: float = 0.0, width: float = 0.0):
        self.height = height
        self.width = width

    def area(self) -> float:
        return self.width * self.height


class Square(Shape):
    def __init__(self, side: float = 0):
        self.side = side

    def area(self):
        return self.side * self.side


rectangle = Rectangle()
rectangle.width = 5
rectangle.height = 10

print("Calcualted area is 5 * 10 = 50")
print(rectangle.area())


square = Square()
square.side = 5

print("Calcualted area is 5 * 5 = 25")
print(square.area())
