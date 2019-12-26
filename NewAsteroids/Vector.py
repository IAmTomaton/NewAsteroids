import math


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        if (other == 0):
            raise ArgumentException('Деление вектора на нуль')
        return Vector(self.x / other, self.y / other)

    def __iadd__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def mod(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_angle(self):
        return math.degrees(math.atan2(self.y, self.x))

    def rotate(self, angle):
        x = self.mod() * math.cos(math.radians(angle + self.get_angle()))
        y = self.mod() * math.sin(math.radians(angle + self.get_angle()))
        return Vector(x, y)

    def angle_between(self, other):
        if self.mod() * other.mod() == 0:
            return 0
        cos = (self.x * other.x + self.y * other.y) /\
              (self.mod() * other.mod())
        angle = math.degrees(math.acos(cos))
        return angle

    def distance(self, other):
        return math.sqrt((self.x - other.x)*(self.x - other.x) +
                         (self.y - other.y)*(self.y - other.y))

    def copy(self):
        return Vector(self.x, self.y)

    def tup(self):
        return self.x, self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
