from unittest.mock import MagicMock
try:
    import pygame
except SystemExit:
    pygame = MagicMock()


class TextureLib:

    def __init__(self):
        self.textures = {}
        self.step = 1

    def init(self):

        basic = pygame.image.load('Textures/Basic.png')

        self.textures['basic'] = [
            pygame.transform.rotate(basic.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]

        asteroid = pygame.image.load("Textures/Asteroid.png")

        self.textures["asteroid_large"] = [
            pygame.transform.rotate(asteroid.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]

        asteroid = pygame.transform\
            .scale(asteroid,
                   (asteroid.get_width()//2, asteroid.get_height()//2))

        self.textures["asteroid_medium"] = [
            pygame.transform.rotate(asteroid.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]

        asteroid = pygame.transform\
            .scale(asteroid,
                   (asteroid.get_width() // 2, asteroid.get_height() // 2))

        self.textures["asteroid_small"] = [
            pygame.transform.rotate(asteroid.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]

        player = pygame.image.load("Textures/Player.png")

        self.textures["player"] = [
            pygame.transform.rotate(player.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]

        bullet = pygame.image.load("Textures/Bullet.png")

        self.textures["bullet"] = [
            pygame.transform.rotate(bullet.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]

        enemy_bullet = pygame.image.load("Textures/Enemy_bullet.png")

        self.textures["enemy_bullet"] = [
            pygame.transform
            .rotate(enemy_bullet.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]

        star_platinum = pygame.image.load('Textures/Star_platinum.png')

        self.textures['star_platinum'] = [
            pygame.transform.rotate(
                star_platinum.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]

        last_hamon = pygame.image.load('Textures/Last_hamon.png')

        self.textures['last_hamon'] = [
            pygame.transform.rotate(last_hamon.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]

        particle = pygame.image.load('Textures/Particle.png')

        self.textures['particle'] = [
            pygame.transform.rotate(particle.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]

        hol_horse = pygame.image.load('Textures/Hol_horse.png')

        self.textures['hol_horse'] = [
            pygame.transform.rotate(hol_horse.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]

        black_hole = pygame.image.load('Textures/Black_Hole.png')

        self.textures['black_hole'] = [
            pygame.transform.rotate(black_hole.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]
