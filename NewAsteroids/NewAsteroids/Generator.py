from Units.Asteroids import Asteroid
from Units.StarPlatinum import StarPlatinum
from Units.LastHamon import LastHamon
from Units.HolHorse import HolHorse
from Units.BlackHole import BlackHole
from Useful import random_value
from Vector import Vector
from Body import Body
from UnitCard import UnitCard


class Generator:

    def __init__(self):
        self.levels = {}
        self.level = []
        self.init_levels()

    def init_levels(self):
        self.init_menu()
        self.init_level_1()
        self.init_level_2()
        self.init_level_3()

    def init_menu(self):
        menu = []
        asteroid_card = UnitCard(Asteroid,
                                 10, 5, 1, 0, 0)
        menu.append(asteroid_card)

        self.levels['menu'] = menu

    def init_level_1(self):
        level_1 = []
        asteroid_card = UnitCard(Asteroid,
                                 6, 8, 1, 0.002, 0.002)
        level_1.append(asteroid_card)

        star_platinum = UnitCard(StarPlatinum,
                                 1, 20, 0, 0, 0)
        level_1.append(star_platinum)

        last_hamon = UnitCard(LastHamon,
                              1, 40, 0, 0, 0)
        level_1.append(last_hamon)

        self.levels['level_1'] = level_1

    def init_level_2(self):
        level_2 = []
        asteroid_card = UnitCard(Asteroid,
                                 6, 8, 1, 0.01, 0.01)
        level_2.append(asteroid_card)

        star_platinum = UnitCard(StarPlatinum,
                                 1, 20, 0, -0.001, 0)
        level_2.append(star_platinum)

        last_hamon = UnitCard(LastHamon,
                              1, 40, 0, -0.001, 0)
        level_2.append(last_hamon)

        hol_horse = UnitCard(HolHorse,
                             1, 30, 1, 0.01, 0.01)
        level_2.append(hol_horse)

        self.levels['level_2'] = level_2

    def init_level_3(self):
        level_3 = []
        asteroid_card = UnitCard(Asteroid,
                                 6, 8, 1, 0.01, 0.01)
        level_3.append(asteroid_card)

        star_platinum = UnitCard(StarPlatinum,
                                 1, 20, 0, -0.001, 0)
        level_3.append(star_platinum)

        last_hamon = UnitCard(LastHamon,
                              1, 40, 0, -0.001, 0)
        level_3.append(last_hamon)

        hol_horse = UnitCard(HolHorse,
                             1, 30, 1, 0.01, 0.01)
        level_3.append(hol_horse)

        hol_horse = UnitCard(BlackHole,
                             1, 60, 1, 0.01, 0.01)
        level_3.append(hol_horse)

        self.levels['level_3'] = level_3

    def update(self, space, delta):
        for unit_card in self.level:
            self.evolution(unit_card, delta)
            self.check_spawn(space, delta, unit_card)

    def check_spawn(self, space, delta, unit_card):
        fault = 0.4
        all_names = unit_card.unit_type.all_names()
        if space.count(all_names) <= unit_card.max_count - 1:
            if unit_card.cooldown < 0:
                self.create_unit(space, unit_card.unit_type, unit_card.rotate)
                unit_card.cooldown = unit_card.delay *\
                    random_value(1 - fault, 1 + fault)
            unit_card.cooldown -= delta

    def evolution(self, unit_card, delta):
        unit_card.delay -= unit_card.delay *\
            unit_card.evolution_time * delta
        unit_card.max_count += unit_card.max_count *\
            unit_card.evolution_count * delta

    def create_unit(self, space, unit_type, rotate):
        body = Body.simple()
        x = 1
        y = 1

        while 0 <= x <= space.size[0] and 0 <= y <= space.size[1]:
            x = random_value(-100, space.size[0] + 100)
            y = random_value(-100, space.size[1] + 100)

        body.coordinates = Vector(x, y)

        velocity = Vector(random_value(30, 100), 0)
        angle = random_value(0, 360)
        velocity = velocity.rotate(angle)
        body.velocity = velocity

        angle_velocity = random_value(-100, 100) * rotate
        body.angel_velocity = angle_velocity

        unit = unit_type.create(body)
        space.add_unit(unit)

    def reset_cooldown(self):
        for unit_card in self.level:
            unit_card.cooldown = unit_card.standart_delay
            unit_card.delay = unit_card.standart_delay

    def level_1(self, space):
        space.clear()
        self.reset_cooldown()
        self.level = self.levels['level_1']

    def level_2(self, space):
        space.clear()
        self.reset_cooldown()
        self.level = self.levels['level_2']

    def level_3(self, space):
        space.clear()
        self.reset_cooldown()
        self.level = self.levels['level_3']

    def menu(self, space):
        space.clear()
        self.reset_cooldown()
        self.level = self.levels['menu']
