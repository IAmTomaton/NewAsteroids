import unittest
from unittest.mock import MagicMock
from Units.Player import Player
from Body import Body


class Test_test_player(unittest.TestCase):

    def test_update(self):
        body = Body.simple()
        player = Player.create(body)
        space = MagicMock()

        player.update(space, 10)

        self.assertTrue(player.live)


if __name__ == '__main__':
    unittest.main()
