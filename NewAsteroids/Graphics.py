from unittest.mock import MagicMock
try:
    import pygame
except SystemExit:
    pygame = MagicMock()
import math


class Graphics:

    def __init__(self, lib):
        self.lib = lib
        self.font_size = 36
        self.colour_button = (200, 250, 250)

    def draw_unit(self, unit):
        x = unit.body.coordinates.x
        y = unit.body.coordinates.y
        angle = int(unit.body.angle // self.lib.step)
        image = self.lib.textures[unit.texture][angle]
        rect = image.get_rect(center=(x, y))
        self.window.blit(image, rect)

    def draw_units(self, units):
        self.window.fill((0, 0, 0))
        for u in units:
            if u.visible:
                self.draw_unit(u)

    def draw_buttons(self, buttons):
        for b in buttons:
            text = self.font.render(b[0], 1, b[1])
            self.window.blit(text, b[2])

    def draw_debug_units(self, units):
        for i in units:
            a1 = (int(i.body.coordinates.x), int(i.body.coordinates.y))
            a2 = (i.body.coordinates.x + i.body.velocity.x,
                  i.body.coordinates.y + i.body.velocity.y)
            pygame.draw.aaline(self.window, (0, 200, 64), a1, a2)

            if i.radius > 0:
                pygame.draw.circle(self.window, (225, 225, 0), a1, i.radius, 1)

    def draw_stats_player(self, player_box):
        health_text = 'heath: ' + str(player_box.player.health)
        health = self.font.render(health_text, 1, self.colour_button)
        self.window.blit(health, (0, self.font_size * 0))

        velocity_text = 'velocity: ' +\
            str(int(player_box.player.body.velocity.mod()))
        velocity = self.font.render(velocity_text, 1, self.colour_button)
        self.window.blit(velocity, (0, self.font_size * 1))

        colldow_text = 'cooldown: ' +\
            str(int(math.ceil(player_box.player.cooldown)))
        cooldown = self.font.render(colldow_text, 1, self.colour_button)
        self.window.blit(cooldown, (0, self.font_size * 2))

        score_text = 'score: ' + str(player_box.score)
        score = self.font.render(score_text, 1, self.colour_button)
        self.window.blit(score, (0, self.font_size * 3))

    def init(self, window):
        self.window = window
        self.lib.init()
        self.font = pygame.font.Font(None, self.font_size)
