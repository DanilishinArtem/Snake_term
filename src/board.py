# from snake import Snake
# from apple import Apple
from . import snake
from . import apple

class Board:
    def __init__(self, width, height):
        self.board = [['0' for _ in range(width)] for _ in range(height)]
    def refresh_board(self, Snake, Apple):
        self.board = [['0' for _ in range(len(self.board))] for _ in range(len(self.board[:][0]))]
        for i in range(len(Snake.body_x)):
            self.board[Snake.body_y[i]][Snake.body_x[i]] = '*'
        self.board[Apple.y][Apple.x] = '+'
    def plot_board(self, Snake):
        print("Current score: " + str(Snake.score))
        for i in range(len(self.board)):
            print(self.board[i])