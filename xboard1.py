import random
from turtle import Turtle


class Board:
    def __init__(self):
        self.t = Turtle()
        self.t.hideturtle()
        self.t.penup()
        self.tiles = [[4, 2, 4, 2], [0, 2, 2, 0], [0, 0, 0, 0], [0, 2, 0, 2]]
        # self.tiles = \
        # [[0, 0, 0, 0],
        # [0, 0, 0, 0],
        # [0, 2, 4, 0],
        # [4, 4, 2, 4]]
        # self.tiles = self.create_board()
        self.init_pos = (-150, 100)

    def create_board(self):
        tmp = []
        for row in range(4):
            tmp.append([0] * 4)
        return tmp

    def print_curr_board(self):
        for i in self.tiles:
            print(i)

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

    def insert_new(self):
        return
        t = self.tiles
        ran_row = random.randrange(0, 3)
        ran_col = random.randrange(0, 3)
        if t[ran_row][ran_col] == 0:
            print(ran_row, ran_col)
            t[ran_row][ran_col] = 2
        else:
            self.insert_new()

    def go_right(self):
        self.print_curr_board()
        self.mirror()
        self.merge_cells_left()
        self.mirror()
        self.insert_new()

    def go_left(self):
        self.print_curr_board()
        self.merge_cells_left()
        self.insert_new()

    def go_up(self):
        direction = 'up'
        self.print_curr_board()
        # flip cell > 90 degree
        self.rotate90()
        self.merge_cells_left()
        self.rotate90()
        self.insert_new()

    def go_down(self):
        direction = 'up'
        # self.print_curr_board()
        self.rotate90()
        self.merge_cells_right()
        self.rotate90()

    def merge_cells_left(self):
        """Merge all rows to the Left."""
        t = self.tiles
        for i in range(len(t)):
            self.shift_left(self.tiles[i])
            print('---------before merge------------')
            self.print_curr_board()
            for j in range(len(t[0])):
                # if (j > 0 and t[i][j - 1] == t[i][j]) or (i > 0 and t[i - 1][j] == t[i][j]):
                if t[i][j - 1] == t[i][j]:
                    print(f'before: check index {t[i]}')
                    t[i][j - 1] += t[i][j]
                    t[i][j] = 0
                    print(f'after : {t[i]}')
            print('---------after merge------------')
            self.print_curr_board()
            self.shift_left(self.tiles[i])
            print('---------after shift------------')
            self.print_curr_board()


    def merge_cells_right(self):
        """Merge all rows to the right."""
        t = self.tiles
        for i in range(len(t)):
            self.shift_right(self.tiles[i])
            self.go_right()
            # for j in range(len(t[0])):
            #     if t[i][j-1] == t[i][j]:
            #         t[i][j] += t[i][j-1]
            #         t[i][j-1] = 0
            # self.shift_right(self.tiles[i])

        print('merge_cells')
        self.print_curr_board()

    def mirror(self):
        for row in self.tiles:
            row.reverse()
        print('mirror')
        for i in self.tiles:
            print(i)

    def shift_left(self, row):
        while 0 in row:
            row.remove(0)
        for k in range(4 - len(row)):
            row.append(0)

    def shift_right(self, row):
        while 0 in row:
            row.remove(0)
        for k in range(4 - len(row)):
            row.insert(k, 0)

    # def shift_board(self):
    #     tmp = self.tiles
    #     print(tmp)
    #     for row in tmp:
    #         while 0 in tmp:
    #             tmp.remove(0)
    #     for k in range(4 - len(tmp)):
    #         tmp.append(0)
    #     print('-------------------------')
    #     direction = 'shift_board'
    #     for i in tmp:
    #         print(i)

    def rotate90(self):
        t = self.tiles
        flipped_array = [[0 for i in range(len(t[0]))] for j in range(len(t))]
        for i in range(len(t)):
            for j in range(len(t)):
                flipped_array[j][i] = t[i][j]

        for i in range(len(t)):
            for j in range(len(t)):
                self.tiles[i][j] = flipped_array[i][j]

        print('---------rotate90----------')
        for i in t:
            print(i)
