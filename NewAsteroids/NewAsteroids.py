from Space import Space
from PlayerBox import PlayerBox
from Generator import Generator
from Graphics import Graphics
from Menu import Menu
from TextureLib import TextureLib


def main():
    player_box = PlayerBox()
    generator = Generator()
    menu = Menu()
    lib = TextureLib()
    graphics = Graphics(lib)
    space = Space(graphics, menu, generator, player_box)
    space.start()


if __name__ == '__main__':
    main()
