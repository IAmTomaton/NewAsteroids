import unittest
from unittest.mock import MagicMock
from Units.HolHorse import HolHorse
from Body import Body


class Test_test_hol_horse(unittest.TestCase):

    def test_collision(self):
        hol_horse = HolHorse(Body.simple())
        other = MagicMock()
        other.texture = "bullet"
        space = MagicMock()

        hol_horse.collision(other, space)

        self.assertFalse(hol_horse.live)


if __name__ == '__main__':
    unittest.main()
