import unittest
from unittest.mock import MagicMock
import Space


class Test_test_space(unittest.TestCase):

    def setUp(self):
        self.pygame = MagicMock()
        Space.pygame = self.pygame
        self.menu = MagicMock()
        self.generator = MagicMock()
        self.graphics = MagicMock()
        self.player_box = MagicMock()
        self.space = Space.Space(self.graphics, self.menu,
                                 self.generator, self.player_box)

    def test_add_unit(self):
        self.space.add_unit(MagicMock())

        self.assertEqual(1, len(self.space.units))


if __name__ == '__main__':
    unittest.main()
