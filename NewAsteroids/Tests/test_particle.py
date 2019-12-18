import unittest
from unittest.mock import MagicMock
from Units.Particle import Particle
from Vector import Vector


class Test_test_particle(unittest.TestCase):

    def test_create_cloud(self):
        space = MagicMock()

        particle = Particle.create_cloud(space, Vector(0, 0))

        self.assertTrue(space.add_unit.called)

    def test_update(self):
        space = MagicMock()
        particle = Particle.create(MagicMock())
        
        particle.update(space, 3)

        self.assertFalse(particle.live)


if __name__ == '__main__':
    unittest.main()
