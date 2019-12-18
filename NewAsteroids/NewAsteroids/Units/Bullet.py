from Body import Body
from Vector import Vector
from Units.Unit import Unit
from Units.Asteroids import Asteroid


class Bullet(Unit):

    def __init__(self, body, parent):
        super().__init__()
        self.body = body
        self.texture = "bullet"
        self.radius = 0
        self.live = True
        self.time_live = 5
        self.parent = parent

    def update(self, space, delta):
        self.time_live -= delta
        distanse = (self.body.coordinates - self.parent.body.coordinates).mod()
        if distanse > self.radius + self.parent.radius + 5:
            self.radius = 5
        if self.time_live <= 0:
            self.live = False

    def collision(self, other, space):
        if other.texture == "player":
            self.live = False
            other.damage(self)
        asteroids = Asteroid.all_names()
        if other.texture == "hol_horse" or other.texture in asteroids:
            self.live = False

    @staticmethod
    def get_bullet(angle, coordinates, parent):
        body = Body.simple()
        body.angle = angle
        body.velocity = Vector(400, 0).rotate(angle)
        body.coordinates = coordinates
        return Bullet(body, parent)
