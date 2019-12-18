from Units.Unit import Unit


class StarPlatinum(Unit):

    def __init__(self, body):
        super().__init__()
        self.texture = 'star_platinum'
        self.visible = True
        self.radius = 25
        self.body = body
        self.live = True
        self.time = 10
        self.delay = 0
        self.player = None

    def update(self, space, delta):
        if not self.visible:
            self.time -= delta
        if self.time < 0:
            self.player.delay = self.delay
            self.live = False

    def collision(self, other, space):
        if other.texture == 'player':
            self.player = other
            self.delay = other.delay
            other.delay = 0.2
            other.cooldown = 0
            self.visible = False
            self.radius = 0

    @staticmethod
    def create(body):
        return StarPlatinum(body)

    @staticmethod
    def all_names():
        return ['star_platinum']
