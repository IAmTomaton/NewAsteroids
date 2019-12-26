import unittest
from Vector import Vector


class Test_test_vector(unittest.TestCase):

    def test_add(self):
        vector1 = Vector(10, 0)
        vector2 = Vector(10, 5)

        result = vector1 + vector2

        self.assertEqual(Vector(20, 5), result)

    def test_angle_between(self):
        vector1 = Vector(10, 0)
        vector2 = Vector(10, 10)

        result = vector1.angle_between(vector2)

        self.assertTrue(44 < result)
        self.assertTrue(46 > result)

    def test_copy(self):
        vector = Vector(10, 0)

        result = vector.copy()

        self.assertEqual(vector, result)

    def test_distance(self):
        vector1 = Vector(10, 0)
        vector2 = Vector(10, 10)

        result = vector1.distance(vector2)

        self.assertEqual(10, result)

    def test_distance(self):
        vector = Vector(10, 0)

        result = vector.tup()

        self.assertEqual((10, 0), result)


if __name__ == '__main__':
    unittest.main()
