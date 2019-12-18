import unittest
from unittest.mock import MagicMock
from Units.StarPlatinum import StarPlatinum
from Body import Body


class Test_test_star_platinum(unittest.TestCase):

    def test_collision(self):
        star_platinum = StarPlatinum(Body.simple())
        other = MagicMock()
        other.texture = "player"
        space = MagicMock()

        star_platinum.collision(other, space)

        self.assertFalse(star_platinum.visible)

    def test_update(self):
        star_platinum = StarPlatinum(Body.simple())
        space = MagicMock()
        other = MagicMock()
        star_platinum.player = other
        star_platinum.visible = False

        star_platinum.update(space, 12)

        self.assertFalse(star_platinum.live)


if __name__ == '__main__':
    unittest.main()
