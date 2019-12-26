import unittest
from unittest.mock import MagicMock
from Body import Body
from Vector import Vector
import Space
import NewAsteroids


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

    def test_update_units(self):
        unit = MagicMock()
        self.space.add_unit(unit)

        self.space.update_units(10)

        self.assertTrue(unit.update.called)

    def test_clear(self):
        unit = MagicMock()
        self.space.add_unit(unit)

        self.space.clear()

        self.assertEqual(0, len(self.space.units))

    def test_move_unit(self):
        unit = MagicMock()
        body = Body.simple()
        body.velocity = Vector(100, 0)
        unit.body = body

        self.space.move_unit(unit, 1)

        self.assertEqual(100, body.coordinates.x)

    def test_check_collision(self):
        unit1 = MagicMock()
        unit1.body = Body.simple()
        unit1.radius = 10
        unit2 = MagicMock()
        unit2.body = Body.simple()
        unit2.radius = 10
        self.space.add_unit(unit1)
        self.space.add_unit(unit2)

        self.space.check_collision()

        self.assertTrue(unit1.collision.called)
        self.assertTrue(unit2.collision.called)

    def test_cleaning(self):
        self.space.add_unit(MagicMock())
        unit = MagicMock()
        unit.live = False
        self.space.add_unit(unit)

        self.space.cleaning()

        self.assertEqual(1, len(self.space.units))

    def test_cleaning(self):
        unit = MagicMock()
        unit.texture = "1"
        self.space.add_unit(unit)

        self.assertEqual(1, self.space.count(["1"]))

    def test_event_handler_down(self):
        event = MagicMock()
        event.type = 1
        self.pygame.KEYDOWN = 1
        self.menu.scene = "play"

        self.space.event_handler(event)

        self.assertFalse(self.menu.esc.called)

    def test_event_handler_up(self):
        event = MagicMock()
        event.type = 1
        self.pygame.KEYUP = 1
        self.menu.scene = "play"

        self.space.event_handler(event)

        self.assertFalse(self.menu.esc.called)

    def test_update_space(self):
        self.space.add_unit(MagicMock())
        unit = MagicMock()
        unit.live = False
        self.space.add_unit(unit)
        self.space.pause = True

        self.space.update_space(10)

        self.assertEqual(1, len(self.space.units))


if __name__ == '__main__':
    unittest.main()
