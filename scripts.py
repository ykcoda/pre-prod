"""
O: Open and Close Principle

Software entities (classes, modules, functions, etc. ) should be open for extension but
closed for modification
"""

from enum import Enum
import math


class ShapeType(Enum):
    CIRCLE = "circle"
    RECTANGLE = "rectangle"


class Shape:

    def __init__(
        self,
        shape_type: ShapeType,
        radius: float = 0,
        height: float = 0,
        width: float = 0,
    ):
        self.type = shape_type
        self.radius = radius
        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        if self.type == ShapeType.CIRCLE:
            return math.pi * self.radius**2
        elif self.type == ShapeType.RECTANGLE:
            return self.height * self.width
        else:
            raise ValueError("Unsupported shape type")


circle = Shape(ShapeType.CIRCLE, radius=5)
rect = Shape(ShapeType.RECTANGLE, height=4, width=6)

print(f"Circle area: {circle.calculate_area()}")
print(f"Reactangle area: {rect.calculate_area()}")
