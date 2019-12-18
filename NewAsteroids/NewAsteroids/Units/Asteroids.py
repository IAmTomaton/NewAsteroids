from Body import Body
from Units.Particle import Particle
from Units.Unit import Unit


class Asteroid(Unit):

    def __init__(self, size, body):
        super().__init__()
        self.size = size
        if size == 3:
            self.texture = 'asteroid_large'
            self.radius = 55
        elif size == 2:
            self.texture = 'asteroid_medium'
            self.radius = 27
        elif size == 1:
            self.texture = 'asteroid_small'
            self.radius = 14

        self.body = body
        self.live = True
        self.visible = True

    @staticmethod
    def large(body):
        return Asteroid(3, body)

    @staticmethod
    def medium(body):
        return Asteroid(2, body)

    @staticmethod
    def small(body):
        return Asteroid(1, body)

    @staticmethod
    def create(body):
        return Asteroid.large(body)

    def update(self, space, delta):
        pass

    def collision(self, other, space):
        if other.texture == 'bullet' or other.texture == "hol_horse":
            self.dead(other, space)
        elif other.texture == 'player' and other.invisible_cooldown < 0:
            other.damage(self)
            self.dead(other, space)

    def dead(self, other, space):
        Particle.create_cloud(space, self.body.coordinates)
        self.live = False
        if self.size > 1:
            self.crash(space)
        space.player_box.score += 1

    def create_chip(self, direction):
        velocity = self.body.velocity.rotate(10 * direction)
        body = Body(self.body.coordinates.copy(), velocity, 0,
                    self.body.angel_velocity, False)
        return Asteroid(self.size - 1, body)

    def crash(self, space):
        asteroid = self.create_chip(1)
        space.add_unit(asteroid)
        asteroid = self.create_chip(-1)
        space.add_unit(asteroid)

    @staticmethod
    def all_names():
        return ['asteroid_large', 'asteroid_medium', 'asteroid_small']
