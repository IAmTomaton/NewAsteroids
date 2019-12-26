import unittest
from unittest.mock import MagicMock
import TextureLib


class Test_test_texture_lib(unittest.TestCase):

    def test_init(self):
        TextureLib.pygame = MagicMock()

        textureLib = TextureLib.TextureLib()

        textureLib.init()


if __name__ == '__main__':
    unittest.main()
