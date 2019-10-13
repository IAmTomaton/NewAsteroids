from Units.Asteroids import Asteroid
from Useful import Body, Vector, random_value


class Generator:
    
    def __init__(self):
        self.stop()

    def stop(self):
        self.cooldown_asteroid = 0

        self.delay_asteroid = 0
        self.max_asteroids = 0

    def update(self, space, delta):
        if space.count("asteroid_large") < self.max_asteroids:
            self.cooldown_asteroid -= delta
            if self.cooldown_asteroid < 0:
                self.creature_asteroid(space)
                self.cooldown_asteroid = self.delay_asteroid

    def creature_asteroid(self, space):
        unit = Asteroid.large(Body.simple())
        x = 1
        y = 1

        while 0 <= x <= space.size[0] and 0 <= y <= space.size[1]:
            x = random_value(-100, space.size[0] + 100)
            y = random_value(-100, space.size[1] + 100)            

        unit.body.coordinates = Vector(x, y)

        velocity = Vector(random_value(30, 100), 0)
        angle = random_value(0, 360)
        velocity = velocity.rotate(angle)
        unit.body.velocity = velocity

        angle_velocity = random_value(-100, 100)
        unit.body.angel_velocity = angle_velocity

        space.add_unit(unit)

    def level_1(self, space):
        space.clear()
        self.stop()

        self.max_asteroids = 6
        self.delay_asteroid = 8

    def menu(self, space):
        space.clear()
        self.stop()

        self.max_asteroids = 10
        self.delay_asteroid = 5
