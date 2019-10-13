from Useful import Body, Vector
from Units.Bullet import Bullet


class Player:
    
    def __init__(self, body):
        self.body = body
        self.texture = "player"
        self.radius = 100
        self.live = True
        self.motion_direction = 0
        self.turn_direction = 0

        self.angel_velocity = 90
        self.acceleration = 40

    def update(self, space, delta):
        self.body.angel_velocity = self.angel_velocity * self.turn_direction

        self.body.velocity += Vector(self.acceleration, 0).rotate(self.body.angle) * self.motion_direction * delta

    def collision(self, other, space):
        pass

class PlayerBox():

    def __init__(self):
        self.play = False
        self.cooldown = 0
        self.delay = 2

    def again(self, space):
        body = Body.simple()
        body.coordinates = Vector(space.size[0] / 2, space.size[1] / 2)
        body.braking = True
        self.player = Player(body)
        self.play = True
        space.add_unit(self.player)

    def stop_game(self):
        self.play = False
        self.player.live = False

    def update(self, space, delta):
        if self.play:
            if not self.player.live:
                self.play = False
            self.cooldown -= delta

    def motion(self, direction):
        if self.play and self.player.live:
            self.player.motion_direction = direction

    def turn(self, direction):
        if self.play and self.player.live:
            self.player.turn_direction = direction

    def shot(self, space):
        if self.play and self.player.live:
            if self.cooldown <= 0:
                space.add_unit(self.get_bullet())
                self.cooldown = self.delay

    def get_bullet(self):
        return Bullet.get_bullet(self.player.body.angle, self.player.body.coordinates)
