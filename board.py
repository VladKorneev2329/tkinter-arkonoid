from settings import *


class Board:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.width = 100
        self.height = 10
        self.speed = 10
        self.id = canvas.create_rectangle(0, 0, self.width, self.height, fill=color)
        self.pos_x = 0
        self.pos_y = 0
        self.pos_point_xy = (self.pos_x, self.pos_y)
        self.canvas.move(self.id, display_width // 2 - self.width / 2, display_height - self.height - 25)

    def  move(self, event):
        self.pos_x = event.x


    def draw(self):
        print(self.canvas.coords(self.id))
        self.canvas.coords(self.id, self.pos_x - self.width//2, display_height - self.height - 25, self.width//2 + self.pos_x, display_height - 25)
