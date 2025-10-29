"""
O: Open and Close Principle

Software entities (classes, modules, functions, etc. ) should be open for extension but
closed for modification
"""

from abc import ABC, abstractmethod
from cmath import rect
from enum import Enum
import math


class ShapeType(Enum):
    CIRCLE = "circle"
    RECTANGLE = "rectangle"


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        return self.height * self.width


class Triangle(Shape):
    def __init__(self, breath: float, height: float):
        self.breath = breath
        self.height = height

    def calculate_area(self):
        return 0.5 * self.breath * self.height


circle = Circle(5)
print(circle.calculate_area())

rect = Rectangle(12, 5)  # noqa
print(rect.calculate_area())


trai = Triangle(12, 5)
print(trai.calculate_area())
# class Shape:

#     def __init__(
#         self,
#         shape_type: ShapeType,
#         radius: float = 0,
#         height: float = 0,
#         width: float = 0,
#     ):
#         self.type = shape_type
#         self.radius = radius
#         self.height = height
#         self.width = width

#     def calculate_area(self) -> float:
#         if self.type == ShapeType.CIRCLE:
#             return math.pi * self.radius**2
#         elif self.type == ShapeType.RECTANGLE:
#             return self.height * self.width
#         else:
#             raise ValueError("Unsupported shape type")


# circle = Shape(ShapeType.CIRCLE, radius=5)
# rect = Shape(ShapeType.RECTANGLE, height=4, width=6)

# print(f"Circle area: {circle.calculate_area()}")
# print(f"Reactangle area: {rect.calculate_area()}")
