import math
import typing

Number = typing.Union[float, int]


class Vector:
    def __init__(self, x: Number, y: Number):
        self.x = x
        self.y = y

    @classmethod
    def down(cls) -> "Vector":
        return cls(0, -1)

    @classmethod
    def up(cls) -> "Vector":
        return cls(0, 1)

    @classmethod
    def left(cls) -> "Vector":
        return cls(-1, 0)

    @classmethod
    def right(cls) -> "Vector":
        return cls(1, 0)

    @classmethod
    def one(cls) -> "Vector":
        return cls(1, 1)

    @classmethod
    def zero(cls) -> "Vector":
        return cls(0, 0)

    @property
    def square_magnitude(self) -> Number:
        return self.x ** 2 + self.y ** 2

    @property
    def magnitude(self) -> Number:
        return math.sqrt(self.square_magnitude)

    @property
    def normalized(self) -> "Vector":
        length = self.magnitude
        if length <= 0:
            raise ValueError("The zero vector cannot be normalized")
        return self.__class__(self.x / length, self.y / length)

    def normalize(self) -> None:
        norm = self.normalized
        self.x = norm.x
        self.y = norm.y

    def angle(self) -> float:
        return math.atan2(self.y, self.x)

    @staticmethod
    def equals(vector1: "Vector", vector2: "Vector") -> bool:
        return vector1 == vector2

    @staticmethod
    def dot_product(vector1: "Vector", vector2: "Vector") -> Number:
        return vector1.x * vector2.x + vector1.y * vector2.y

    @staticmethod
    def clamp_magnitude(vector: "Vector", max_length: Number):
        magnitude = vector.magnitude
        ratio = 1
        if magnitude > max_length:
            ratio = max_length / vector.magnitude
        return vector * ratio

    @staticmethod
    def distance(vector1: "Vector", vector2: "Vector") -> Number:
        x = vector1.x - vector2.x
        y = vector1.y - vector2.y
        return math.sqrt(x ** 2 + y ** 2)

    @staticmethod
    def angle_between(vector1: "Vector", vector2: "Vector") -> Number:
        """ Returns angle between vectors in radians in interval [-PI, PI]"""
        return math.atan2(vector2.y, vector2.x) - \
            math.atan2(vector1.y, vector1.x)

    @staticmethod
    def lerp(vector1: "Vector", vector2: "Vector", amount: float) -> "Vector":
        x = vector1.x * (1 - amount) + vector2.x * amount
        y = vector1.y * (1 - amount) + vector2.y * amount
        return vector1.__class__(x, y)

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise IndexError(item)

    def __repr__(self):
        name = f"{self.__class__.__module__}.{self.__class__.__qualname__}"
        return f"{name}({self.x}, {self.y})"

    def __str__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y})"

    # region Add overload
    def __add__(self, other):
        if type(other) != type(self):
            return NotImplemented
        return self.__class__(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)
    # endregion

    # region Sub overload
    def __sub__(self, other):
        if type(other) != type(self):
            return NotImplemented
        return self.__class__(self.x - other.x, self.y - other.y)

    def __rsub__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)
    # endregion

    # region Mul overload
    def __mul__(self, other):
        if type(other) not in (int, float):
            return NotImplemented
        return self.__class__(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)
    # endregion

    # region Truediv overload
    def __truediv__(self, other):
        if type(other) not in (int, float):
            return NotImplemented
        return self.__class__(self.x / other, self.y / other)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)
    # endregion

    def __neg__(self):
        return self.__class__(-self.x, -self.y)

    def __eq__(self, other):
        return type(other) == type(self) and \
               self.x == other.x and self.y == other.y
