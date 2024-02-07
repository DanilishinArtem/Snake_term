# from board import Board
# from apple import Apple
from . import board
from . import apple

class Snake:
    def __init__(self, x, y, dir):
        self.head_x = x
        self.head_y = y
        self.dir = dir
        self.body_x = [x, x]
        self.body_y = [y + 1, y]
        self.alive = True
        self.score = 0
    def make_move(self, Board, Apple):
        if self.dir == 'up':
            self.move_up(Board, Apple)
        elif self.dir == 'down':
            self.move_down(Board, Apple)
        elif self.dir == 'left':
            self.move_left(Board, Apple)
        elif self.dir == 'right':
            self.move_right(Board, Apple)
    def move_left(self, Board, Apple):
        if self.head_x == 0:
            self.alive = False
        else:
            self.head_x -= 1
            self.body_x.append(self.head_x)
            self.body_y.append(self.head_y)
            if self.head_x == Apple.x and self.head_y == Apple.y:
                self.score += 1
                Apple.add_apple(Board)
                # Board.refresh_board(self, Apple)
            else:
                self.body_x.pop(0)
                self.body_y.pop(0)
    def move_right(self, Board, Apple):
        if self.head_x == len(Board.board[0]) - 1:
            self.alive = False
        else:
            self.head_x += 1
            self.body_x.append(self.head_x)
            self.body_y.append(self.head_y)
            if self.head_x == Apple.x and self.head_y == Apple.y:
                self.score += 1
                Apple.add_apple(Board)
                # Board.refresh_board(self, Apple)
            else:
                self.body_x.pop(0)
                self.body_y.pop(0) 
    def move_up(self, Board, Apple):
        if self.head_y == 0:
            self.alive = False
        else:
            self.head_y -= 1
            self.body_x.append(self.head_x)
            self.body_y.append(self.head_y)
            if self.head_x == Apple.x and self.head_y == Apple.y:
                self.score += 1
                Apple.add_apple(Board)
                # Board.refresh_board(self, Apple)
            else:
                self.body_x.pop(0)
                self.body_y.pop(0) 
    def move_down(self, Board, Apple):
        if self.head_y == len(Board.board) - 1:
            self.alive = False
        else:
            self.head_y += 1
            self.body_x.append(self.head_x)
            self.body_y.append(self.head_y)
            if self.head_x == Apple.x and self.head_y == Apple.y:
                self.score += 1
                Apple.add_apple(Board)
                # Board.refresh_board(self, Apple)
            else:
                self.body_x.pop(0)
                self.body_y.pop(0) 