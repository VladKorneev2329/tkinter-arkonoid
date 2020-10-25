from tkinter import *
import time
from settings import *
from ball import Ball
from board import Board

# Создаем объект окна
root = Tk()
# Задаем окну название
root.title(display_title)
# Запрещаем менять размер оена
# root.resizable(0, 0)
root.wm_attributes('-topmost', 1)

canvas = Canvas(root, width=display_width, height=display_height, highlightthickness=0)
canvas.pack()
root.update()

board = Board(canvas, 'blue')
ball = Ball(canvas, 'red', board)
# balls = [Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#          Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#         Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#         Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#         Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#         Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#         Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#         Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#         Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#         Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#         Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#         Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#         Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board),
#          Ball(canvas, random.choice(colours), board), Ball(canvas, random.choice(colours), board)]
canvas.bind('<Motion>', board.move)
while True:
    # for ball in balls:
    #     ball.draw()
    ball.draw()
    board.draw()
    root.update_idletasks()
    root.update()
    time.sleep(1/60)
