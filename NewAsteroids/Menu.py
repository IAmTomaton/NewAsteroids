from Button import Button
try:
    import pygame
except SystemExit:
    pygame = MagicMock()


class Menu(object):

    def __init__(self):
        self.scene = ""
        self.indent = 150
        self.menu_scenes = {}
        self.buttons = []
        self.init_scenes()
        self.index = 0

    def init_scenes(self):
        main_menu = []
        play = Button(self.levels, (self.indent, 100), "PLAY")
        main_menu.append(play)
        records = Button(self.records, (self.indent, 150), "RECORDS")
        main_menu.append(records)
        resolution = Button(self.resolution, (self.indent, 200), "RESOLUTION")
        main_menu.append(resolution)
        exit = Button(self.exit, (self.indent, 250), "EXIT")
        main_menu.append(exit)
        self.menu_scenes["main_menu"] = main_menu

        self.menu_scenes["play"] = []

        levels = []
        back = Button(self.main_menu_from_menu, (self.indent, 100), 'BACK')
        levels.append(back)
        level_1 = Button(self.level_1, (self.indent, 150), 'LEVEL 1')
        levels.append(level_1)
        level_2 = Button(self.level_2, (self.indent, 200), 'LEVEL 2')
        levels.append(level_2)
        level_3 = Button(self.level_3, (self.indent, 250), 'LEVEL 3')
        levels.append(level_3)
        self.menu_scenes['levels'] = levels

        game_menu = []
        continue_b = Button(self.continue_c, (self.indent, 100), "CONTINUE")
        game_menu.append(continue_b)
        save = Button(self.save_record, (self.indent, 150), "SAVE")
        game_menu.append(save)
        menu = Button(self.main_menu, (self.indent, 200), "MAIN MENU")
        game_menu.append(menu)
        self.menu_scenes["game_menu"] = game_menu

        save_record = []
        menu = Button(self.main_menu, (self.indent, 100), 'MAIN MENU')
        save_record.append(menu)
        save = Button(self.save, (self.indent, 150), 'SAVE')
        save_record.append(save)
        name = Button(None, (self.indent, 200), 'NAME: ')
        save_record.append(name)
        self.menu_scenes['save_record'] = save_record

        resolution = []
        back = Button(self.main_menu_from_menu, (self.indent, 100), 'BACK')
        resolution.append(back)
        resolution1 = Button(lambda space: space.set_resolution((1200, 800)),
                      (self.indent, 150), '1200x800')
        resolution.append(resolution1)
        resolution2 = Button(lambda space: space.set_resolution((1000, 600)),
                      (self.indent, 200), '1000x600')
        resolution.append(resolution2)
        resolution3 = Button(lambda space: space.set_resolution((800, 500)),
                      (self.indent, 250), '800x500')
        resolution.append(resolution3)
        self.menu_scenes['resolution'] = resolution

    def main_menu(self, space):
        self.scene = "main_menu"
        self.buttons = self.menu_scenes["main_menu"]
        self.index = 0
        space.generator.menu(space)
        space.player_box.stop_game()
        space.pause = False

    def main_menu_from_menu(self, space):
        self.scene = "main_menu"
        self.buttons = self.menu_scenes["main_menu"]
        self.index = 0

    def levels(self, space):
        self.scene = 'levels'
        self.buttons = self.menu_scenes['levels']
        self.index = 0

    def play(self, space):
        self.scene = "play"
        self.buttons = self.menu_scenes["play"]
        self.index = 0

    def resolution(self, space):
        self.scene = 'resolution'
        self.buttons = self.menu_scenes['resolution']
        self.index = 0

    def level_1(self, space):
        self.play(space)
        space.generator.level_1(space)
        space.player_box.again(space)

    def level_2(self, space):
        self.play(space)
        space.generator.level_2(space)
        space.player_box.again(space)

    def level_3(self, space):
        self.play(space)
        space.generator.level_3(space)
        space.player_box.again(space)

    def records(self, space):
        self.scene = 'records'
        self.index = 0
        self.buttons = []
        records = []
        with open('records.txt', 'r') as f:
            for i in f:
                player = i[:-1].split(' ')
                records.append((player[0], player[1]))

        records.sort(reverse=True)

        self.buttons.append(Button(self.main_menu_from_menu,
                                   (self.indent, 100), "BACK"))

        for i in range(0, min(len(records), 10)):
            text = str(int(records[i][0]) - 10000) +\
                ' ' + records[i][1]
            self.buttons.append(
                Button(None, (self.indent, 150 + 50 * i), text))

    def save_record(self, space):
        self.scene = 'save_record'
        self.index = 0
        self.buttons = self.menu_scenes['save_record']
        self.buttons[2].text = 'NAME: '

    def save(self, space):
        with open('records.txt', 'a') as records:
            length = len(self.buttons[2].text[6:])
            name = self.buttons[2].text[6:] if length > 0 else 'nameless'
            records.write(
                str(space.player_box.score + 10000) + ' ' + name + '\n')
        self.main_menu(space)

    def exit(self, space):
        space.exit()

    def continue_c(self, space):
        self.scene = "play"
        self.buttons = self.menu_scenes["play"]
        self.index = 0
        space.pause = False

    def enter(self, space):
        if 0 <= self.index < len(self.buttons):
            if self.buttons[self.index].action is not None:
                self.buttons[self.index].action(space)

    def arrow(self, direction):
        if 0 <= self.index + direction < len(self.buttons):
            self.index += direction

    def esc(self, space):
        if self.scene == "play":
            self.scene = "game_menu"
            self.buttons = self.menu_scenes["game_menu"]
            self.index = 0
            space.pause = True

    def key_down(self, key):
        if self.scene == 'save_record':
            self.buttons[2].text += key

    def delete(self):
        if self.scene == 'save_record' and len(self.buttons[2].text) > 6:
            self.buttons[2].text = self.buttons[2].text[:-1]

    def get_buttons(self):
        for i in range(len(self.buttons)):
            color = (200, 250, 250)
            if i == self.index:
                color = (255, 0, 0)
            yield self.buttons[i].text, color, self.buttons[i].position
