from Units.Unit import Unit


class LastHamon(Unit):

    def __init__(self, body):
        super().__init__()
        self.texture = 'last_hamon'
        self.visible = True
        self.radius = 25
        self.body = body
        self.live = True

    def update(self, space, delta):
        pass

    def collision(self, other, space):
        if other.texture == 'player':
            other.health += 1
            self.live = False

    @staticmethod
    def create(body):
        return LastHamon(body)

    @staticmethod
    def all_names():
        return ['last_hamon']
