import pygame
from threading import Thread
from time import time
import sys, random
from TextureLid import TextureLib
from Asteroids import Asteroid
from Useful import Body, Vector
from Player import PlayerBox


class Space(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.live = True
        self.units = []
        self.clock = pygame.time.Clock()
        self.last_time = 0
        self.size = (640, 480)
        self.player_box = PlayerBox()

    def add_unit(self, unit):
        self.units.append(unit)

    def move_unit(self, unit, delta):
        unit.body.coordinates += unit.body.velocity * delta
        unit.body.angle += unit.body.angel_velocity * delta

    def draw_unit(self, unit):
        x = unit.body.coordinates.x
        y = unit.body.coordinates.y
        image = \
            self.lib.textures[unit.texture][int(unit.body.angle // self.lib.step)]
        rect = image.get_rect(center=(x, y))
        self.window.blit(image, rect)

    def move_units(self, delta):
        for u in self.units:
            self.move_unit(u, delta)

    def update_units(self):
        for u in self.units:
            u.update(self)

    def draw_units(self):
        self.window.fill((0, 0, 0))
        for u in self.units:
            self.draw_unit(u)
        pygame.display.update()

    def check_collision(self):
        for u1 in self.units:
            for u2 in self.units:
                if u1 != u2:
                    distance = (u1.body.coordinates - u2.body.coordinates).mod()
                    if u1.radius + u2.radius >= distance:
                        u1.collision(u2, self)

    def event_handler(self):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif i.type == pygame.KEYDOWN:
                unit = Asteroid.large(Body.simple())
                unit.body.velocity = Vector(50, 0)
                self.add_unit(unit)

    def run(self) -> None:
        self.window = pygame.display.set_mode(self.size)
        self.lib = TextureLib()

        while True:
            now_time = time()
            delta = now_time - self.last_time
            self.last_time = now_time

            self.event_handler()

            self.move_units(delta)

            self.check_collision()

            self.update_units()

            self.draw_units()

            self.clock.tick(60)
