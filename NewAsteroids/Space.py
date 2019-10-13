import pygame
from threading import Thread
from time import time
import sys, random
from TextureLid import TextureLib
from Useful import Body, Vector
from Units.Player import PlayerBox
from Units.Asteroids import Asteroid
from Generator import Generator
from Menu import Menu


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

    def add_unit(self, unit):
        self.units.append(unit)

    def move_unit(self, unit, delta):
        unit.body.coordinates += unit.body.velocity * delta
        unit.body.angle = (unit.body.angle + unit.body.angel_velocity * delta) % 360

        if unit.body.coordinates.x > self.size[0]:
            unit.body.coordinates.x = 0
        elif unit.body.coordinates.x < 0:
            unit.body.coordinates.x = self.size[0]

        if unit.body.coordinates.y > self.size[1]:
            unit.body.coordinates.y= 0
        elif unit.body.coordinates.y < 0:
            unit.body.coordinates.y = self.size[1]

        if unit.body.braking:
            if unit.body.velocity.mod() > 0:
                delta_velocity = Vector(self.friction, 0).rotate(unit.body.velocity.get_angle()) * delta
                if delta_velocity.mod() >= unit.body.velocity.mod():
                    unit.body.velocity = Vector(0, 0)
                else:
                    unit.body.velocity -= delta_velocity

        if unit.body.velocity.mod() > self.max_velocity:
            unit.body.velocity = unit.body.velocity / unit.body.velocity.mod() * self.max_velocity

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

    def update_units(self, delta):
        for u in self.units:
            u.update(self, delta)

    def draw_units(self):
        self.window.fill((0, 0, 0))
        for u in self.units:
            self.draw_unit(u)

    def check_collision(self):
        for u1 in self.units:
            for u2 in self.units:
                if u1 != u2:
                    distance = (u1.body.coordinates - u2.body.coordinates).mod()
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

    def count(self, name):
        count = 0
        for i in self.units:
            if i.texture == name:
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
                elif i.key == pygame.K_l:
                    self.debug = not self.debug
                elif self.menu.scene == "play":
                    if i.key == pygame.K_UP:
                        self.player_box.motion(1)
                    elif i.key == pygame.K_DOWN:
                        self.player_box.motion(-1)
                    elif i.key == pygame.K_LEFT:
                        self.player_box.turn(-1)
                    elif i.key == pygame.K_RIGHT:
                        self.player_box.turn(1)
                    elif i.key == pygame.K_SPACE:
                        self.player_box.shot(self)
                elif i.key == pygame.K_UP:
                    self.menu.arrow(-1)
                elif i.key == pygame.K_DOWN:
                    self.menu.arrow(1)
            elif i.type == pygame.KEYUP:
                if self.menu.scene == "play":
                    if i.key == pygame.K_UP:
                        self.player_box.motion(0)
                    elif i.key == pygame.K_DOWN:
                        self.player_box.motion(0)
                    elif i.key == pygame.K_LEFT:
                        self.player_box.turn(0)
                    elif i.key == pygame.K_RIGHT:
                        self.player_box.turn(0)

    def exit(self):
        sys.exit(0)

    def update_space(self, delta):
        font = pygame.font.Font(None, 36)

        self.event_handler()

        if not self.pause:
            self.move_units(delta)

            self.check_collision()
            
            self.update_units(delta)

        self.player_box.update(self, delta)

        self.draw_units()

        self.draw_buttons(font)

        if self.debug:
            self.draw_debug()

        pygame.display.update()

        self.cleaning()

    def draw_buttons(self, font):
        for b in self.menu.get_text():
            text = font.render(b[0], 1, b[1])
            self.window.blit(text, b[2])

    def draw_debug(self):
        for i in self.units:
            a1 = (int(i.body.coordinates.x), int(i.body.coordinates.y))
            a2 = (i.body.coordinates.x + i.body.velocity.x,
                  i.body.coordinates.y + i.body.velocity.y)
            pygame.draw.aaline(self.window, (0, 200, 64), a1, a2)

            pygame.draw.circle(self.window, (225, 225, 0), a1, i.radius, 1)

    def run(self) -> None:
        self.window = pygame.display.set_mode(self.size)
        self.lib = TextureLib()
        pygame.init()

        while True:
            now_time = time()
            delta = now_time - self.last_time
            self.last_time = now_time

            self.update_space(delta)

            self.generator.update(self, delta)

            self.clock.tick(60)
