import unittest
from unittest.mock import MagicMock
from PlayerBox import PlayerBox


class Test_test_player_box(unittest.TestCase):

    def test_again(self):
        player_box = PlayerBox()
        space = MagicMock()

        player_box.again(space)

        self.assertTrue(space.add_unit.called)
        self.assertTrue(player_box.play)

    def test_stop_game(self):
        player_box = PlayerBox()

        player_box.stop_game()

        self.assertEqual(0, player_box.score)
        self.assertFalse(player_box.play)

    def test_update(self):
        player_box = PlayerBox()
        space = MagicMock()
        player_box.again(space)

        player_box.update(space, 10)

        self.assertEqual(0, player_box.score)
        self.assertTrue(player_box.play)


if __name__ == '__main__':
    unittest.main()
