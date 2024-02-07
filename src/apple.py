# from board import Board
from . import board
import numpy as np

class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add_apple(self, Board):
        coordinates = []
        for i in range(len(Board.board)):
            for j in range(len(Board.board[i])):
                if Board.board[i][j] != '+' and Board.board[i][j] != '*':
                    coordinates.append([i, j])
        index = np.random.randint(0, len(coordinates))
        self.x = coordinates[index][0]
        self.y = coordinates[index][1]