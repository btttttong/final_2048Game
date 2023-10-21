import time

from board import Board
from turtle import Screen

screen = Screen()
screen.setup(600, 600)
screen.listen()
screen.tracer(0)

board = Board()
is_game_on = True

screen.onkeypress(fun=board.go_up, key="Up")
screen.onkeypress(fun=board.go_down, key="Down")
screen.onkeypress(fun=board.go_right, key="Right")
screen.onkeypress(fun=board.go_left, key="Left")

while is_game_on:
    time.sleep(1)
    screen.update()
    board.draw_tiles()


screen.mainloop()