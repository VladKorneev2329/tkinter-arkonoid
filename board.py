from settings import *
class Board:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.width = 100
        self.height = 10
        self.speed = 4
        self.id = canvas.create_rectangle(0, 0, self.width, self.height , fill=color)
        self.pos_x = 1
        self.pos_y = 0
        self.canvas.move(self.id, display_width // 2 - self.width / 2, display_height - self.height - 5)

    def draw(self):
        self.canvas.move(self.id, self.pos_x, self.pos_y)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.pos_x = self.speed
        elif pos[2] >= display_height:
            self.pos_x = -self.speed

    def move