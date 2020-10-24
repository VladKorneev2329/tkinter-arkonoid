import random
import time, sys
from settings import *


class Ball:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.speed = 4
        self.radius = random.randrange(15, 36)
        self.id = canvas.create_oval(10, 10, self.radius, self.radius, fill=color)
        self.canvas.move(self.id, random.randrange(0, display_width), 250)
        self.pos_x = random.randrange(-4, 4)
        self.pos_y = random.randrange(1, 4)


    def draw(self):
        self.canvas.move(self.id, self.pos_x, self.pos_y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.pos_y = self.speed
        elif pos[3] >= display_height:
            self.pos_y = -self.speed
            # time.sleep(3)
            # sys.exit()

        if pos[0] <= 0:
            self.pos_x = self.speed
        elif pos[2] >= display_width:
            self.pos_x = -self.speed