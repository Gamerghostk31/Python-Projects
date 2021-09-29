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

def try_to_place_ship_on_board():
    pass

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