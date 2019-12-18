import unittest
from Body import Body
from Vector import Vector


class Test_test_body(unittest.TestCase):

    def test_simple(self):
        body = Body.simple()

        self.assertEqual(Vector(0, 0), body.coordinates)
        self.assertEqual(Vector(0, 0), body.velocity)
        self.assertEqual(0, body.angle)
        self.assertEqual(0, body.angel_velocity)

    def test_angle(self):
        body = Body.simple()

        body.angle = 740

        self.assertEqual(20, body.angle)


if __name__ == '__main__':
    unittest.main()
