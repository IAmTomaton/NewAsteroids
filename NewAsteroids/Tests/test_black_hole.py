import unittest
from unittest.mock import MagicMock
from Units.BlackHole import BlackHole
from Body import Body


class Test_test_black_hole(unittest.TestCase):

    def test_collision(self):
        black_hole = BlackHole.create(Body.simple())
        other = MagicMock()
        space = MagicMock()

        black_hole.collision(other, space)

        self.assertFalse(other.live)

    def test_update(self):
        black_hole = BlackHole.create(Body.simple())
        space = MagicMock()

        black_hole.update(space, 100)

        self.assertFalse(black_hole.live)


if __name__ == '__main__':
    unittest.main()
