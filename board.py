import random
from turtle import Turtle
# i = row
# j = col
BOARD_METRIX = 4

class Board:
    def __init__(self):
        self.t = Turtle()
        self.t.hideturtle()
        self.t.penup()
        # self.tiles = [[4, 2, 4, 2], [0, 2, 2, 0], [0, 0, 0, 0], [0, 2, 0, 2]]
#         self.tiles = [[2, 8, 2, 4],
# [16, 4, 32, 2],
# [64, 8, 4, 16],
# [128, 4, 8, 2]]
        self.tiles = [[0] * BOARD_METRIX for i in range(BOARD_METRIX)]
        self.insert_new()
        self.insert_new()
        self.init_pos = (-150, 100)
        self.score = 0
        try:
            f = open("highscore.txt", "r")
            self.highscore = int(f.read())
            f.close()
        except ValueError:
            self.highscore = 0


    def print_curr_board(self):
        for i in self.tiles:
            print(i)

    def draw_tiles(self):
        t = self.t
        t.clear()
        t.goto(0,150)
        t.write(f'Score = {self.score} | HighScore = {self.highscore}', align='center', font=('Tahoma', 20, 'normal'))
        t.goto(self.init_pos)
        for row in range(BOARD_METRIX):
            for col in range(BOARD_METRIX):
                t.goto(t.xcor() + 50, t.ycor())
                t.write(self.tiles[row][col], align='center', font=('Tahoma', 20, 'normal'))
            t.goto(t.xcor() - 200, t.ycor() - 50)

    def insert_new(self):
        t = self.tiles
        if any(0 in row for row in t):
            ran_row = random.randrange(0, 3)
            ran_col = random.randrange(0, 3)
            while t[ran_row][ran_col] != 0:
                ran_row = random.randint(0, 3)
                ran_col = random.randint(0, 3)
            print(f'-----insert new to this position [{[ran_row]},{[ran_col]}]-------')
            t[ran_row][ran_col] = 2

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
        self.print_curr_board()
        self.rotate90()
        self.merge_cells_left()
        self.rotate90()
        self.insert_new()

    def go_down(self):
        direction = 'up'
        self.print_curr_board()
        self.rotate90()
        self.merge_cells_right()
        self.rotate90()
        self.insert_new()


    def mirror(self):
        for row in self.tiles:
            row.reverse()
        print('mirror')
        for i in self.tiles:
            print(i)

    def merge_cells_left(self):
        """Merge all rows to the Left."""
        t = self.tiles
        for i in range(BOARD_METRIX):
            self.shift_left(self.tiles[i])
            for j in range(BOARD_METRIX):
                # if (j > 0 and t[i][j - 1] == t[i][j]) or (i > 0 and t[i - 1][j] == t[i][j]):
                if t[i][j - 1] == t[i][j]:
                    t[i][j - 1] += t[i][j]
                    self.add_score(t[i][j-1])
                    t[i][j] = 0
                    print(f'after : {t[i]}')
            self.shift_left(self.tiles[i])

    def shift_left(self, row):
        while 0 in row:
            row.remove(0)
        for k in range(BOARD_METRIX - len(row)):
            row.append(0)

    def shift_right(self, row):
        while 0 in row:
            row.remove(0)
        for k in range(BOARD_METRIX - len(row)):
            row.insert(k, 0)

    def rotate90(self):
        t = self.tiles
        flipped_array = [[0 for i in range(BOARD_METRIX)] for j in range(BOARD_METRIX)]
        for i in range(BOARD_METRIX):
            for j in range(BOARD_METRIX):
                flipped_array[j][i] = t[i][j]

        for i in range(BOARD_METRIX):
            for j in range(BOARD_METRIX):
                self.tiles[i][j] = flipped_array[i][j]

        print('---------rotate90----------')
        self.print_curr_board()

    def merge_cells_right(self):
        """Merge all rows to the right."""
        t = self.tiles
        for i in range(BOARD_METRIX):
            self.shift_right(self.tiles[i])
            self.go_right()

    def add_score(self, score):
        print(f'-----------------------curr = {self.score} | high = {self.highscore}')
        self.score += score
        #fixme: incorrect condition to increment score
        if self.score >= self.highscore:
            with open("highscore.txt", "w") as f:
                self.highscore = self.score
                f.write(str(self.highscore))

    def is_game_over(self):
        t = self.tiles
        turtle = self.t
        if any(0 in row for row in t):
            return True
        else:
            for row in range(BOARD_METRIX):
                for col in range(BOARD_METRIX):
                    if row < BOARD_METRIX - 1 and t[row][col] == t[row + 1][col]:
                        return True
                    if col < BOARD_METRIX - 1 and t[row][col] == t[row][col + 1]:
                        return True
            print('*****Game Over*****')
            turtle.penup()
            turtle.goto(0, 0)
            turtle.write("Game Over!", align="center", font=("Tahoma", 80, "normal"))
            return False

        return True
