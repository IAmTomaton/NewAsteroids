from Units.Unit import Unit


class BlackHole(Unit):

    def __init__(self, body):
        super().__init__()
        self.texture = 'black_hole'
        self.radius = 35
        self.body = body
        self.time = 30
        self.gravity = 10000

    def update(self, space, delta):
        self.time -= delta
        if self.time < 0:
            self.live = False
        for unit in space.units:
            vector_from_unit = (unit.body.coordinates - self.body.coordinates)
            if vector_from_unit.mod() != 0:
                direction = vector_from_unit / vector_from_unit.mod()
                acseleration = -self.gravity / vector_from_unit.mod()
                unit.body.velocity += direction * acseleration * delta

    def collision(self, other, space):
        if other.texture == "player":
            other.damage(self)
            return
        other.live = False

    @staticmethod
    def create(body):
        return BlackHole(body)

    @staticmethod
    def all_names():
        return ['black_hole']
