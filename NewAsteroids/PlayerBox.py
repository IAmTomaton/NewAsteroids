from Body import Body
from Vector import Vector
from Units.Bullet import Bullet
from Units.Player import Player


class PlayerBox():

    def __init__(self):
        self.play = False
        self.player = None
        self.score = 0

    def again(self, space):
        self.score = 0
        body = Body.simple()
        body.coordinates = Vector(space.size[0] / 2, space.size[1] / 2)
        body.braking = True
        self.player = Player(body)
        self.play = True
        space.add_unit(self.player)

    def stop_game(self):
        self.play = False
        if self.player is not None:
            self.player.live = False
        self.score = 0

    def update(self, space, delta):
        if self.play:
            if not self.player.live:
                self.death(space)

    def death(self, space):
        self.play = False
        space.menu.save_record(space)

    def motion(self, direction):
        if self.play and self.player.live:
            self.player.motion_direction = direction

    def turn(self, direction):
        if self.play and self.player.live:
            self.player.turn_direction = direction

    def shot(self, shoots):
        if self.play and self.player.live:
            self.player.shot(shoots)
