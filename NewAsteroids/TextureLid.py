import pygame


class TextureLib:

    def __init__(self):
        self.textures = {}
        self.step = 3

        asteroid = pygame.image.load("Textures/Asteroid.png")

        self.textures["asteroid_large"] = [
            pygame.transform.rotate(asteroid.convert_alpha(), -i * self.step)
            for i in range(0, int(360 / self.step))]
