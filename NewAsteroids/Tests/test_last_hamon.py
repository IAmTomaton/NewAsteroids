import unittest
from unittest.mock import MagicMock
from Units.LastHamon import LastHamon
from Vector import Vector
from Body import Body


class Test_test_last_hamon(unittest.TestCase):

    def test_collision(self):
        space = MagicMock()
        last_hamon = LastHamon.create(Body.simple())
        other = MagicMock()
        other.texture = "player"

        last_hamon.collision(other, space)

        self.assertFalse(last_hamon.live)


if __name__ == '__main__':
    unittest.main()
