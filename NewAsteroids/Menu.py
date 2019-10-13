from enum import Enum
import pygame


class Button:

    def __init__(self, action, position, text):
        self.action = action
        self.position = position
        self.text = text

    def click(self, menu, space):
        self.action(menu, space)


class Menu(object):

    def __init__(self, space):
        self.scene = ""
        self.menu_scenes = {}
        self.buttons = []
        self.init_scenes()
        self.index = 0
        Menu.main_menu(self, space)

    def init_scenes(self):
        main_menu = []
        play = Button(Menu.play, (100, 100), "PLAY")
        main_menu.append(play)
        records = Button(Menu.records, (100, 150), "RECORDS")
        main_menu.append(records)
        exit = Button(Menu.exit, (100, 200), "EXIT")
        main_menu.append(exit)
        self.menu_scenes["main_menu"] = main_menu

        self.menu_scenes["play"] = []

        game_menu = []
        continue_b = Button(Menu.continue_c, (100, 100), "CONTINUE")
        game_menu.append(continue_b)
        menu = Button(Menu.main_menu_from_game, (100, 150), "MAIN MENU")
        game_menu.append(menu)
        self.menu_scenes["game_menu"] = game_menu

    @staticmethod
    def main_menu(menu, space):
        menu.scene = "main_menu"
        menu.buttons = menu.menu_scenes["main_menu"]
        menu.index = 0
        space.generator.menu(space)

    @staticmethod
    def main_menu_from_game(menu, space):
        menu.scene = "main_menu"
        menu.buttons = menu.menu_scenes["main_menu"]
        menu.index = 0
        space.generator.menu(space)
        space.player_box.stop_game()
        space.pause = False

    @staticmethod
    def play(menu, space):
        menu.scene = "play"
        menu.buttons = menu.menu_scenes["play"]
        menu.index = 0
        space.generator.level_1(space)

        space.player_box.again(space)

    @staticmethod
    def records(menu, space):
        print("records")

    @staticmethod
    def exit(menu, space):
        space.exit()

    @staticmethod
    def continue_c(menu, space):
        menu.scene = "play"
        menu.buttons = menu.menu_scenes["play"]
        menu.index = 0
        space.pause = False

    def enter(self, space):
        if self.index < len(self.buttons):
            self.buttons[self.index].action(self, space)

    def arrow(self, direction):
        if 0 <= self.index + direction < len(self.buttons):
            self.index = self.index + direction

    def esc(self, space):
        if not self.scene == "play":
            return
        self.scene = "game_menu"
        self.buttons = self.menu_scenes["game_menu"]
        self.index = 0
        space.pause = True

    def get_text(self):
        for i in range(len(self.buttons)):
            color = (255, 255, 255)
            if i == self.index:
                color = (255, 0, 0)
            yield self.buttons[i].text, color, self.buttons[i].position
