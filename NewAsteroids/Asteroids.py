class Asteroid:

    def __init__(self, size, body):
        if (size == 1):
            self.texture = "asteroid_large"
            self.radius = 100

        self.body = body

    @staticmethod
    def large(body):
        return Asteroid(1, body)

    def update(self, space):
        pass

    def collision(self, other, space):
        print(1)
