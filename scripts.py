"""
L: Listov Substitution Principle (LSP)

Object of a superclass should be replacable with objects of its subclass without affecting the correctness
of the program
"""

from abc import ABC, abstractmethod
from cmath import rect


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, height: float = 0.0, width: float = 0.0):
        self._height = height
        self._width = width

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side: float = 0):
        super().__init__(side, side)

    @Rectangle.width.setter
    def width(self, value: float):
        self._width = value
        self._height = value

    @Rectangle.height.setter
    def height(self, value: float):
        self._width = value
        self._height = value


rectangle = Square()
rectangle.width = 5
rectangle.height = 10

print("Calcualted area is 5 * 10 = 50")
print(rectangle.area())
