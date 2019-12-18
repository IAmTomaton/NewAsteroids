import pygame
from threading import Thread
from time import time
import sys
import random
from TextureLid import TextureLib
from Graphics import Graphics
from Body import Body
from Vector import Vector
from PlayerBox import PlayerBox
from Units.Asteroids import Asteroid
from Generator import Generator
from Menu import Menu
import math


class Space(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.live = True
        self.units = []
        self.clock = pygame.time.Clock()
        self.last_time = 0
        self.size = (1200, 800)
        self.player_box = PlayerBox()
        self.generator = Generator()
        self.menu = Menu(self)
        self.pause = False
        self.friction = 20
        self.max_velocity = 300
        self.debug = False
        self.font_size = 36

    def add_unit(self, unit):
        self.units.append(unit)

    def move_unit(self, unit, delta):
        unit.body.coordinates += unit.body.velocity * delta
        unit.body.angle =\
            (unit.body.angle + unit.body.angel_velocity * delta) % 360

        if unit.body.coordinates.x > self.size[0]:
            unit.body.coordinates.x = 0
        elif unit.body.coordinates.x < 0:
            unit.body.coordinates.x = self.size[0]

        if unit.body.coordinates.y > self.size[1]:
            unit.body.coordinates.y = 0
        elif unit.body.coordinates.y < 0:
            unit.body.coordinates.y = self.size[1]

        if unit.body.braking:
            if unit.body.velocity.mod() > 0:
                delta_velocity = Vector(
                    self.friction, 0).rotate(
                        unit.body.velocity.get_angle()) * delta
                if delta_velocity.mod() >= unit.body.velocity.mod():
                    unit.body.velocity = Vector(0, 0)
                else:
                    unit.body.velocity -= delta_velocity

        if unit.body.velocity.mod() > self.max_velocity:
            unit.body.velocity = unit.body.velocity /\
                unit.body.velocity.mod() * self.max_velocity

    def move_units(self, delta):
        for u in self.units:
            self.move_unit(u, delta)

    def update_units(self, delta):
        for u in self.units:
            u.update(self, delta)

    def check_collision(self):
        for u1 in self.units:
            for u2 in self.units:
                if u1 != u2 and u1.radius > 0 and u2.radius > 0:
                    distance = (
                        u1.body.coordinates - u2.body.coordinates).mod()
                    if u1.radius + u2.radius >= distance:
                        u1.collision(u2, self)

    def cleaning(self):
        i = 0
        while i < len(self.units):
            if not self.units[i].live:
                self.units.pop(i)
            else:
                i += 1

    def clear(self):
        self.units = []

    def count(self, names):
        count = 0
        for n in names:
            for i in self.units:
                if i.texture == n:
                    count += 1
        return count

    def event_handler(self):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                self.exit()

            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_RETURN:
                    self.menu.enter(self)
                elif i.key == pygame.K_ESCAPE:
                    self.menu.esc(self)
                elif i.key == pygame.K_LALT:
                    self.debug = not self.debug
                elif self.menu.scene == "play":
                    if i.key == pygame.K_UP or i.key == pygame.K_w:
                        self.player_box.motion(1)
                    elif i.key == pygame.K_DOWN or i.key == pygame.K_s:
                        self.player_box.motion(-1)
                    elif i.key == pygame.K_LEFT or i.key == pygame.K_a:
                        self.player_box.turn(-1)
                    elif i.key == pygame.K_RIGHT or i.key == pygame.K_d:
                        self.player_box.turn(1)
                    elif i.key == pygame.K_SPACE:
                        self.player_box.shot(True)
                elif i.key == pygame.K_UP:
                    self.menu.arrow(-1)
                elif i.key == pygame.K_DOWN:
                    self.menu.arrow(1)
                elif i.key == pygame.K_BACKSPACE:
                    self.menu.delete()
                elif i.key != pygame.K_SPACE:
                    key = pygame.key.name(i.key).upper()
                    self.menu.key_down(key)
            elif i.type == pygame.KEYUP:
                if self.menu.scene == "play":
                    if i.key == pygame.K_UP or i.key == pygame.K_w:
                        self.player_box.motion(0)
                    elif i.key == pygame.K_DOWN or i.key == pygame.K_s:
                        self.player_box.motion(0)
                    elif i.key == pygame.K_LEFT or i.key == pygame.K_a:
                        self.player_box.turn(0)
                    elif i.key == pygame.K_RIGHT or i.key == pygame.K_d:
                        self.player_box.turn(0)
                    elif i.key == pygame.K_SPACE:
                        self.player_box.shot(False)

    def exit(self):
        sys.exit(0)

    def update_space(self, delta):
        self.event_handler()

        if not self.pause:
            self.move_units(delta)

            self.check_collision()

            self.update_units(delta)

        self.player_box.update(self, delta)

        self.graphics.draw_units(self.units)

        self.graphics.draw_buttons(self.menu.get_buttons())

        if self.player_box.play:
            self.graphics.draw_stats_player(self.player_box)

        if self.debug:
            self.graphics.draw_debug_units(self.units)

        pygame.display.update()

        self.cleaning()

    def run(self) -> None:
        self.window = pygame.display.set_mode(self.size)
        pygame.init()

        self.graphics = Graphics(self.window)

        while True:
            now_time = time()
            delta = now_time - self.last_time
            self.last_time = now_time

            self.update_space(delta)

            self.generator.update(self, delta)

            self.clock.tick(60)
