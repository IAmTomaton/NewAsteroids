import unittest
from unittest.mock import MagicMock
from Units.Bullet import Bullet
from Vector import Vector


class Test_test_bullet(unittest.TestCase):

    def test_update(self):
        parent = MagicMock()
        parent.radius = 1
        bullet = Bullet.get_bullet(10, Vector(0, 0), parent)

        bullet.update(MagicMock(), 6)

        self.assertFalse(bullet.live)

    def test_collision(self):
        space = MagicMock()
        parent = MagicMock()
        bullet = Bullet.get_bullet(10, Vector(0, 0), parent)
        other = MagicMock()
        other.texture = "player"

        bullet.collision(other, space)

        self.assertFalse(bullet.live)


if __name__ == '__main__':
    unittest.main()
