import unittest
from unittest.mock import MagicMock, Mock
from Generator import Generator
from Units.Unit import Unit
from UnitCard import UnitCard


class Test_test_generator(unittest.TestCase):

    def test_init_levels(self):
        generator = Generator()

        generator.init_levels()

    def test_level_1(self):
        generator = Generator()
        space = MagicMock()
        generator.init_levels()

        generator.level_1(space)

        self.assertTrue(space.clear.called)

    def test_level_2(self):
        generator = Generator()
        space = MagicMock()
        generator.init_levels()

        generator.level_2(space)

        self.assertTrue(space.clear.called)

    def test_level_3(self):
        generator = Generator()
        space = MagicMock()
        generator.init_levels()

        generator.level_3(space)

        self.assertTrue(space.clear.called)

    def test_menu(self):
        generator = Generator()
        space = MagicMock()
        generator.init_levels()

        generator.menu(space)

        self.assertTrue(space.clear.called)

    def test_create_unit(self):
        generator = Generator()
        space = MagicMock()
        space.size = (10, 10)
        generator.init_levels()

        generator.create_unit(space, Unit, 100)

        self.assertTrue(space.add_unit.called)

    def test_create_unit(self):
        def count(arg):
            return 0
        generator = Generator()
        space = MagicMock()
        space.count = count
        space.size = (10, 10)
        card = UnitCard(Unit, 1, 60, 1, 0.01, 0.01)
        generator.init_levels()

        generator.check_spawn(space, 100, card)
        generator.check_spawn(space, 100, card)

        self.assertTrue(space.add_unit.called)

    def test_evolution(self):
        generator = Generator()
        card = UnitCard(Unit, 1, 60, 1, 0.01, 0.01)

        generator.evolution(card, 100)

        self.assertEqual(2, card.max_count)


if __name__ == '__main__':
    unittest.main()
