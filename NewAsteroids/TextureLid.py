import pygame


class TextureLib:

    def __init__(self):
        self.textures = {}
        self.step = 1

        asteroid = pygame.image.load("Textures/Asteroid.png")

        self.textures["asteroid_large"] = [
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
