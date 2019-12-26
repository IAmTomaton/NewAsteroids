import unittest
from unittest.mock import MagicMock
from Units.Asteroids import Asteroid
from Body import Body


class Test_test_asteroid(unittest.TestCase):

    def test_collision(self):
        body = Body.simple()
        asteroid = Asteroid.create(body)
        other = MagicMock()
        other.texture = 'player'
        other.invisible_cooldown = -1
        space = MagicMock()

        asteroid.collision(other, space)

        self.assertFalse(asteroid.live)


if __name__ == '__main__':
    unittest.main()
