import random
from turtle import Turtle


class Board:
    def __init__(self):
        self.t = Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.tiles = [[4, 2, 4, 2], [0, 2, 2, 0], [0, 0, 0, 0], [0, 2, 0, 0]]
        # self.tiles = self.create_board()
        self.init_pos = (-200, 0)

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
        ran_row = random.randrange(0,3)
        ran_col = random.randrange(0, 3)
        if t[ran_row][ran_col] == 0:
            t[ran_row][ran_col] = 2
        else:
            self.insert_new(1)

    def go_right(self):
        direction = 'right'
        print(direction)
        # print(self.tiles)
        for i in self.tiles:
            print(i)
        self.arrange()
        self.merge_cells(direction)
        self.arrange()
        self.insert_new(0)

    def go_left(self):
        direction = 'left'
        for i in self.tiles:
            print(i)
        self.arrange_l()
        self.merge_cells(direction)
        self.arrange_l()
        self.insert_new(3)

    def go_up(self):
        direction = 'up'
        for i in self.tiles:
            print(i)
        self.arrange_up()
        self.merge_cells(direction)
        self.arrange_up()
        # self.insert_new(3)


    def arrange(self):
        t = self.tiles
        for i in range(len(t)):
            for j in range(len(t)):
                t[i].sort()
        print('---------------------')
        print('t')
        for i in self.tiles:
            print(i)

    def arrange_l(self):
        t = self.tiles
        for i in range(len(t)):
            for j in range(len(t)):
                t[i].sort(reverse=True)
        print('---------------------')
        print('arrange_l')
        for i in self.tiles:
            print(i)

    def arrange_up(self):
        t = self.tiles
        flipped_array = [[0 for i in range(len(t[0]))] for j in range(len(t))]
        for i in range(len(t)):
            for j in range(len(t)):
                flipped_array[j][i] = t[i][j]

        print('---------------------')
        print('flip')
        # self.tilees = flipped_array
        for i in range(len(t)):
            for j in range(len(t)):
                self.tiles[i][j] = flipped_array[i][j]
        for i in t:
            print(i)


        self.arrange_l()
        self.merge_cells('left')

        for i in range(len(t)):
            for j in range(len(t)):
                flipped_array[j][i] = t[i][j]

        print('---------------------')
        print('last swap')
        for i in flipped_array:
            print(i)


    def merge_cells(self, direction):
        t = self.tiles
        if direction == 'right' or direction == 'left':
            for i in range(len(t)):
                for j in range(len(t[0])):
                    if t[i][j - 1] == t[i][j]:
                        t[i][j - 1] += t[i][j]
                        t[i][j] = 0
        elif direction == 'up':
            print('merge_cells_up')

        # elif direction == 'left':
        #     for j in range(len(t[0])):
        #         for i in range(len(t)):
        #             try:
        #                 if t[i][j-1] == t[i][j]:
        #                     t[i][j-1] *= t[i][j]
        #                     t[i][j] = 0
        #             except:
        #                 pass

        print('---------------------')
        print('merge_cells')
        for i in self.tiles:
            print(i)

    def m(self):
        for i in self.tiles:
            i.reverse()






