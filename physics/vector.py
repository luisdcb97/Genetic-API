import math
import typing

Number = typing.Union[float, int]


class Vector:
    def __init__(self, x: Number, y: Number):
        self.x = x
        self.y = y

    @classmethod
    def down(cls):
        return cls(0, -1)

    @classmethod
    def up(cls):
        return cls(0, 1)

    @classmethod
    def left(cls):
        return cls(-1, 0)

    @classmethod
    def right(cls):
        return cls(1, 0)

    @classmethod
    def one(cls):
        return cls(1, 1)

    @classmethod
    def zero(cls):
        return cls(0, 0)

    @property
    def square_magnitude(self):
        return self.x ** 2 + self.y ** 2

    @property
    def magnitude(self):
        return math.sqrt(self.square_magnitude)

    @property
    def normalized(self):
        length = self.magnitude
        if length <= 0:
            raise ValueError("The zero vector cannot be normalized")
        return Vector(self.x / length, self.y / length)

    def normalize(self):
        norm = self.normalized
        self.x = norm.x
        self.y = norm.y

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
