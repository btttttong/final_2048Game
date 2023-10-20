import random
from turtle import Turtle


class Board:
    def __init__(self):
        self.t = Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.tiles = [[0, 0, 0, 0], [0, 2, 2, 0], [0, 0, 0, 0], [0, 2, 0, 0]]
        # self.tiles = self.create_board()
        self.init_pos = (-200, 0)

    # def __str__(self):
    #     rv = ''
    #     for row in self.board:
    #         rv += ''.join('.o'[c] for c in row)
    #         rv += '\n'
    #     return rv

    def create_board(self):
        tmp = []
        for row in range(4):
            tmp.append([0] * 4)
        return tmp

    def draw_tiles(self):
        t = self.t
        t.clear()
        t = self.t
        self.t.goto(self.init_pos)
        for row in range(len(self.tiles)):
            # print(row)
            for col in range(len(self.tiles[row])):
                # print(' ', self.tiles[row][col])
                t.goto(t.xcor() + 50, t.ycor())
                t.write(self.tiles[row][col], align='center', font=('Tahoma', 20, 'normal'))
            t.goto(t.xcor() - 200, t.ycor() - 50)

    # def init_state(self):

    def insert_new(self, index):
        t = self.tiles
        ran = random.randrange(0,3)
        print(ran)
        if t[index][ran] == 0:
            t[ran][index] = 2

    def go_right(self):
        print('hello')
        print(self.tiles)
        self.arrange()
        self.merge_cells()
        self.arrange()
        self.insert_new(0)

    def arrange(self):
        t = self.tiles
        for i in range(len(t)):
            for j in range(len(t)):
                t[i].sort()

        print('arrange = ', t)

    def merge_cells(self):
        t = self.tiles
        for i in range(len(t)):
            for j in range(len(t[0])):
                if t[i][j - 1] == t[i][j]:
                    t[i][j - 1] += t[i][j]
                    t[i][j] = 0

        print('merge_cells = ', t)



