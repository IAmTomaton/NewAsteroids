from Vector import Vector


class Body:

    def __init__(self, coordinates, velocity, angle, angel_velocity, braking):
        self.coordinates = coordinates
        self.velocity = velocity

        self._angle = 0
        self.angle = angle
        self.angel_velocity = angel_velocity

        self.braking = braking

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value % 360

    @staticmethod
    def simple():
        return Body(Vector(0, 0), Vector(0, 0), 0, 0, False)
