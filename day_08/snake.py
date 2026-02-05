# goal: print out our board that doesnt have a snake yet. a board is a width by height string of .'s. We want this reprinting every tick

import keyboard
import sys
import os
import time
import random

class Game:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.game_over = False
        self.game_started = False
        self.snake_positions = [(5,5)]
        self.fruit_position = (2,2)
        self.snake = 'X '
        self.fruit = '🍎'
        self.delta = (0,0)
        self.grow_snake = False
        self.end_game_message = ""

        # List[List[Str]]
        self.board = self.make_board()
        
        keyboard.add_hotkey('r', self.restart)
        keyboard.add_hotkey('up', self.move_up)
        keyboard.add_hotkey('down', self.move_down)
        keyboard.add_hotkey('left', self.move_left)
        keyboard.add_hotkey('right', self.move_right)
        pass

    def render(self, board_str):
        sys.stdout.write("\033[H\033[J")  # cursor home + clear screen
        sys.stdout.write(board_str)
        sys.stdout.flush()

    def move_up(self):
        self.delta = (-1,0)
        
    def move_down(self):
        self.delta = (1,0)
        
    def move_left(self):
        self.delta = (0,-1)
       
    def move_right(self):
        self.delta = (0,1)
    
    def snake_movement(self):
        head_position = self.snake_positions[0]

        new_head = (
            head_position[0] + self.delta[0],
            head_position[1] + self.delta[1]
        )

        # out of bounds check
        if not (0 <= new_head[0] < self.height and 0 <= new_head[1] < self.width):
            self.end_game_message = "You went out of bounds, sorry! Game over!"
            self.restart()
            return

        # self-collision check
        if new_head in self.snake_positions[1:]:
            self.end_game_message = "You ran into yourself, sorry! Game over!"
            self.restart()
            return

        # move snake
        self.snake_positions.insert(0, new_head)

        # handle tail
        if self.grow_snake:
            self.grow_snake = False
        else:
            self.snake_positions.pop()


        
    # will return the list of lists that is the game board
    def make_board(self):
        board = []

        for j in range(self.height):
            board.append([])

        for inner_list_j in range(len(board)):
            inner_list = board[inner_list_j]

            for i in range(self.width):
                inner_list.append('. ')

        return board

    def create_board_string(self):
        # OUTPUT what the user sees (Front end, GUI)
        board_string = ''
        for i in range(len(self.board)):
            inner_list = self.board[i]
            for j in range(len(inner_list)):
                board_string += inner_list[j]
            board_string += '\n'
        return board_string

    
    def run_game(self):
        while not self.game_over:
            self.print_snake()
            self.print_fruit()
            board_string = self.create_board_string()
            #os.system("clear")   # macOS/Linux
            self.render(board_string)
            time.sleep(0.1)
            snake_head = self.snake_positions[0]
            if self.fruit_position[0] == snake_head[0] and self.fruit_position[1] == snake_head[1]:
                self.eat_fruit()
            self.snake_movement()

    def eat_fruit(self):
        new_fruit_position = list(self.fruit_position)
        new_fruit_position[0] = random.randint(0,self.width-1)
        new_fruit_position[1] = random.randint(0,self.height-1)
        self.fruit_position = tuple(new_fruit_position)
        self.grow_snake = True
        self.print_fruit()

    def print_fruit(self):
        fruit = self.fruit
        fruit_position = self.fruit_position
        row = fruit_position[0]
        column = fruit_position[1]        
        self.board[row][column] = fruit
    
    def print_snake(self):
         # Clear the board
        self.board = self.make_board()

        #loop through each element of snake positions and add the snake body into the board at that position
        for position in self.snake_positions:
            x = position[0]
            y = position[1]
            self.board[x][y] = "X "
            
    def restart(self):
        print(f'Game Over: {self.end_game_message}')
        self.game_over = True        
        


game = Game(30, 30)

game.run_game()