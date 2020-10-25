import random
import sys
import time

from settings import *


class Ball:

    def __init__(self, canvas, color, board):
        self.board = board
        self.canvas = canvas
        self.speed = 4
        self.radius = random.randrange(20, 30)
        self.id = canvas.create_oval(10, 10, self.radius, self.radius, fill=color)
        self.canvas.move(self.id, board.pos_x, board.pos_y)
        self.pos_x = random.randrange(-4, 4)
        self.pos_y = random.randrange(-4, -1)

    def draw(self):
        self.canvas.move(self.id, self.pos_x, self.pos_y)
        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:
            self.pos_y = self.speed
        elif pos[3] >= display_height:
            time.sleep(3)
            sys.exit()

        if pos[0] <= 0:
            self.pos_x = self.speed
        elif pos[2] >= display_width:
            self.pos_x = -self.speed

        if self.board.canvas.coords(self.board.id)[1] <= self.canvas.coords(self.id)[3] and \
                self.board.canvas.coords(self.board.id)[1] >= self.canvas.coords(self.id)[3] - self.board.height:

            if self.board.canvas.coords(self.board.id)[0] <= self.canvas.coords(self.id)[2] and \
                    self.canvas.coords(self.id)[0] <= self.board.canvas.coords(self.board.id)[2]:
                self.pos_y = -self.speed
