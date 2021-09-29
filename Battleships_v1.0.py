# Author: Basson Koch
# Project Name: Battleships
# Description: 

# Modules
import random
import time

# Global Variables
board = [[]]
board_size = 10
ship_positions = [[]]
num_of_ships = 6
ammo = 50
num_ships_sunk = 0
game_over = False
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def create_board():
    
    global board
    global board_size
    global num_of_ships
    global ship_positions
    
    random.seed(time.time())
    
    # Set length of rows and cols to the board size (10)
    rows, cols = (board_size, board_size)
    
    board = []
    # Vertical Rows
    for r in range(rows):
        row = []
        # Horzontal Columns
        for c in range(cols):
            row.append(".")
        board.append(row)

    num_of_ships_placed = 0
    
    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        # If method returns true, place a ship on the board and add 1 to num of ships placed
        if try_to_place_ship_on_board(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1

def try_to_place_ship_on_board(row, col, direction, length):
    
    global board_size
    # If they return false, loop will replay with new random positions
    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1, col
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1
    
    elif direction == "right":
        if col + length >= board_size:
            return False
        end_col = col + length
        
    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1
        
    elif direction == "down":
        if row + length >= board_size:
            return False
        end_row = row + length
    
    return validate_board_and_place_ship(start_row, end_row, start_col, end_col) 

def validate_board_and_place_ship(start_row, end_row, start_col, end_col):
    
    global board
    global ship_positions
    
    no_errors = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            # for the postisions on the board check if there is another thing in that position
            if board[r][c] != ".":
                no_errors = False
                break
    if no_errors:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_col):
            for c in range(start_col, end_col):
                # If there is nothing in that position, place a ship there
                board[r][c] = "O"
    return no_errors

def main():
    
    print("""
                    Welcome to...          
          _                                    
         |_)  _. _|_ _|_ |  _   _ |_  o ._   _ 
         |_) (_|  |_  |_ | (/_ _> | | | |_) _> 
                                        |      
        ________________________________________
                    By Basson Koch
        ________________________________________
           """)
    
    print("You have 50 rounds of ammo to sink 6 ships... Goodluck!")
    
    create_board()
    
    
    
    

if __name__ == '__main__':
    main()