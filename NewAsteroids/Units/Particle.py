from Body import Body
from Vector import Vector
from Useful import random_value
from Units.Unit import Unit


class Particle(Unit):

    def __init__(self, body):
        super().__init__()
        self.texture = 'particle'
        self.visible = True
        self.radius = 0
        self.body = body
        self.live = True
        self.time = 2

    def update(self, space, delta):
        self.time -= delta
        if self.time < 0:
            self.live = False

    @staticmethod
    def create_cloud(space, position):
        count = 10
        for i in range(10):
            body = Body.simple()

            body.coordinates = position

            angle = random_value(0, 360)
            velocity = random_value(30, 120)
            body.velocity = Vector(velocity, 0).rotate(angle)

            particle = Particle(body)
            space.add_unit(particle)

    @staticmethod
    def create(body):
        return Particle(body)
