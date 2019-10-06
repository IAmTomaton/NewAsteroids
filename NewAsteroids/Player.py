class Player:
    
    def __init__(self, body):
        self.body = body
        self.texture = "player"
        self.radius = 100

    def update(self):
        pass

    def collision(self):
        pass

class PlayerBox():

    def __init__(self):
        pass

    def again(self):
        self.player = Player()
