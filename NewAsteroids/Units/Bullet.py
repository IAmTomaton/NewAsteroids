from Useful import Body, Vector


class Bullet:

    def __init__(self, body):
        self.body = body
        self.texture = "bullet"
        self.radius = 100
        self.live = True

    def update(self, space, delta):
        pass

    def collision(self, other, space):
        pass

    @staticmethod
    def get_bullet(angle, coordinates):
        body = Body.simple()
        body.angle = angle
        body.velocity = Vector(400, 0).rotate(angle)
        body.coordinates = coordinates
        return Bullet(body)
