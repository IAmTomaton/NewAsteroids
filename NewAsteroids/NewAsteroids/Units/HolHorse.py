from Body import Body
from Units.Particle import Particle
from Units.Unit import Unit
from Units.Bullet import Bullet
from Units.Asteroids import Asteroid
from Vector import Vector
import math


class HolHorse(Unit):

    def __init__(self, body):
        super().__init__()
        self.texture = 'hol_horse'
        self.radius = 30
        self.body = body

        self.delay = 5
        self.cooldown = self.delay

        self.max_angle_velocity = 10
        self.max_velocity = 100

    @staticmethod
    def create(body):
        return HolHorse(body)

    def fire(self, space):
        coordinates = self.body.coordinates
        space.add_unit(Bullet.get_bullet(self.body.angle, coordinates, self))

    def update(self, space, delta):
        player_body = space.player_box.player.body

        vector_to_player = player_body.coordinates - self.body.coordinates

        self.body.angle = vector_to_player.get_angle()
        if (player_body.coordinates - self.body.coordinates).mod() < 300:
            velocity = Vector(-self.max_velocity, 0)
            self.body.velocity = velocity.rotate(vector_to_player.get_angle())
        elif (player_body.coordinates - self.body.coordinates).mod() > 400:
            velocity = Vector(self.max_velocity, 0)
            self.body.velocity = velocity.rotate(vector_to_player.get_angle())

        self.cooldown -= delta
        if self.cooldown < 0:
            self.fire(space)
            self.cooldown = self.delay

    def collision(self, other, space):
        if other.texture == 'bullet' or other.texture in Asteroid.all_names():
            Particle.create_cloud(space, other.body.coordinates)
            self.live = False
        elif other.texture == 'player':
            other.damage(self)
            Particle.create_cloud(space, other.body.coordinates)
            self.live = False

    @staticmethod
    def all_names():
        return ['hol_horse']
