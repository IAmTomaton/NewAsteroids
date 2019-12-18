import unittest
from unittest.mock import MagicMock
import Graphics


class Test_test_graphics(unittest.TestCase):

    def setUp(self):
        self.pygame = MagicMock()
        Graphics.pygame = self.pygame
        self.lib = MagicMock()
        self.window = MagicMock()
        self.graphics = Graphics.Graphics(self.lib)
        self.graphics.init(self.window)

    def test_init(self):

        self.graphics.init(MagicMock())

        self.assertTrue(self.lib.init.called)

    def test_draw_stats_player(self):

        self.graphics.draw_stats_player(MagicMock())

        self.assertEqual(4, self.window.blit.call_count)

    def test_draw_unit(self):

        self.graphics.draw_unit(MagicMock())

        self.assertTrue(self.window.blit.called)

    def test_draw_buttons(self):
        button = MagicMock()

        self.graphics.draw_buttons([button, button])

        self.assertTrue(self.window.blit.called)

    def test_draw_units(self):
        button = MagicMock()

        self.graphics.draw_units([button, button])

        self.assertTrue(self.window.blit.called)

    def test_draw_debug_units(self):
        button = MagicMock()
        button.radius = 0

        self.graphics.draw_debug_units([button, button])

        self.assertTrue(self.pygame.draw.aaline.called)


if __name__ == '__main__':
    unittest.main()
