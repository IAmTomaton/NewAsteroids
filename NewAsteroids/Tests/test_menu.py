import unittest
from unittest.mock import MagicMock
import Menu


class Test_test_menu(unittest.TestCase):

    def setUp(self):
        self.pygame = MagicMock()
        Menu.pygame = self.pygame
        self.menu = Menu.Menu()

    def test_init_scenes(self):
        self.menu.init_scenes()

    def test_main_menu(self):
        space = MagicMock()

        self.menu.main_menu(space)

        self.assertTrue(space.generator.menu.called)
        self.assertTrue(space.player_box.stop_game)

    def test_main_menu_from_menu(self):
        space = MagicMock()

        self.menu.main_menu_from_menu(space)

        self.assertEqual("main_menu", self.menu.scene)

    def test_levels(self):
        space = MagicMock()

        self.menu.levels(space)

        self.assertEqual("levels", self.menu.scene)

    def test_play(self):
        space = MagicMock()

        self.menu.play(space)

        self.assertEqual("play", self.menu.scene)

    def test_level_1(self):
        space = MagicMock()

        self.menu.level_1(space)

        self.assertTrue(space.generator.level_1.called)
        self.assertTrue(space.player_box.again)

    def test_level_2(self):
        space = MagicMock()

        self.menu.level_2(space)

        self.assertTrue(space.generator.level_2.called)
        self.assertTrue(space.player_box.again)

    def test_level_3(self):
        space = MagicMock()

        self.menu.level_3(space)

        self.assertTrue(space.generator.level_3.called)
        self.assertTrue(space.player_box.again)

    def test_save_record(self):
        space = MagicMock()

        self.menu.save_record(space)

        self.assertEqual("save_record", self.menu.scene)

    def test_exit(self):
        space = MagicMock()

        self.menu.exit(space)

        self.assertTrue(space.exit.called)

    def test_continue_c(self):
        space = MagicMock()

        self.menu.continue_c(space)

        self.assertFalse(space.pause)
        self.assertEqual("play", self.menu.scene)


if __name__ == '__main__':
    unittest.main()
