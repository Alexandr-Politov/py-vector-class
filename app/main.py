from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            x: int | float = 1.0,
            y: int | float = 1.0
    ) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) ->\
            Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self .y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        scalar_mult = self.x * other.x + self.y * other.y
        abs_self = (self.x ** 2 + self.y ** 2) ** 0.5
        abs_other = (other.x ** 2 + other.y ** 2) ** 0.5
        cos_a = scalar_mult / (abs_self * abs_other)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        radians_cos = math.cos(radians)
        radians_sin = math.sin(radians)
        new_x = self.x * radians_cos - self.y * radians_sin
        new_y = self.x * radians_sin + self.y * radians_cos
        return Vector(new_x, new_y)
