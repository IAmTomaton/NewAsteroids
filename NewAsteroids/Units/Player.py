from Body import Body
from Vector import Vector
from Units.Bullet import Bullet
from Units.Unit import Unit


class Player(Unit):

    def __init__(self, body):
        super().__init__()
        self.body = body
        self.texture = "player"
        self.radius = 15
        self.live = True
        self.visible = True
        self.motion_direction = 0
        self.turn_direction = 0

        self.angel_velocity = 180
        self.acceleration = 100

        self.cooldown = 0
        self.delay = 2

        self.shoots = False

        self.health = 3
        self.invisible_delay = 2
        self.invisible_cooldown = -1

    def update(self, space, delta):
        self.body.angel_velocity = self.angel_velocity * self.turn_direction

        self.body.velocity += Vector(self.acceleration, 0).rotate(
            self.body.angle) * self.motion_direction * delta

        if self.shoots and self.cooldown <= 0:
            space.add_unit(self.get_bullet())
            self.cooldown = self.delay

        if self.cooldown >= 0:
            self.cooldown -= delta

        if self.invisible_cooldown > 0:
            if int(self.invisible_cooldown * 16) % 2 == 1:
                self.visible = False
            else:
                self.visible = True
            self.invisible_cooldown -= delta
        else:
            self.visible = True
            self.invisible_cooldown = -1

    def damage(self, other):
        if self.invisible_cooldown < 0:
            self.health -= 1
            self.invisible_cooldown = self.invisible_delay
        if self.health <= 0:
            self.live = False

    def shot(self, shoots):
        self.shoots = shoots

    def get_bullet(self):
        return Bullet.get_bullet(self.body.angle, self.body.coordinates, self)
