class Button:

    def __init__(self, action, position, text):
        self.action = action
        self.position = position
        self.text = text

    def click(self, menu, space):
        self.action(menu, space)
