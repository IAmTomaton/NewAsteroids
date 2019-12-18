from Body import Body


class Unit:

    def __init__(self):
        self.body = Body.simple()
        self.texture = 'basic'
        self.radius = 0
        self.live = True
        self.visible = True

    def update(self, space, delta):
        pass

    def collision(self, other, space):
        pass

    @staticmethod
    def create(body):
        return Unit()

    @staticmethod
    def all_names():
        return []
