import os
import time
import numpy as np
import keyboard
from src.apple import Apple
from src.board import Board
from src.snake import Snake



print("Hello let's start the game")

width = 20 # input("Enter width: ")
height = 20 # input("Enter height: ")
Board_game = Board(width, height)
Apple_game = Apple(int(np.random.randint(0, width)), int(np.random.randint(0, height/2)))
Snake_game = Snake(int(np.random.randint(0, width)), int(np.random.randint(height/2, height)), 'up')
Board_game.refresh_board(Snake_game, Apple_game)
Board_game.plot_board(Snake_game)

while True:
    if Snake_game.alive == True:
        if keyboard.is_pressed('up'):
            if Snake_game.body_y[len(Snake_game.body_y) - 1] - 1 != Snake_game.body_y[len(Snake_game.body_y) - 2]:
                Snake_game.dir = 'up'
        elif keyboard.is_pressed('down'):
            if Snake_game.body_y[len(Snake_game.body_y) - 1] + 1 != Snake_game.body_y[len(Snake_game.body_y) - 2]:
                Snake_game.dir = 'down'
        elif keyboard.is_pressed('left'):
            if Snake_game.body_x[len(Snake_game.body_x) - 1] - 1 != Snake_game.body_x[len(Snake_game.body_x) - 2]:
                Snake_game.dir = 'left'
        elif keyboard.is_pressed('right'):
            if Snake_game.body_x[len(Snake_game.body_x) - 1] + 1 != Snake_game.body_x[len(Snake_game.body_x) - 2]:
                Snake_game.dir = 'right'
        elif keyboard.is_pressed('esc'):
            break

        os.system('cls')
        Snake_game.make_move(Board_game, Apple_game)
        Board_game.refresh_board(Snake_game, Apple_game)
        Board_game.plot_board(Snake_game)
        time.sleep(0.05)
    else:
        print("Игра окончена, вы проиграли")
        break