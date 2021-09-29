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

def print_board():
    
    global board
    global alphabet
    
    dev_mode = True
    
    alphabet = alphabet[0: len(board) + 1]
    
    for row in range(len(board)):
        print(alphabet[row], end=") ")
        for col in range(len(board[row])):
            if board[row][col] == "O":
                if dev_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(board[row][col], end=" ")
        print("")

def accept_valid_bullet_placement():
    
    global alphabet
    global board
    
    no_errors_with_shot = False
    row = -1
    col = -1
    while no_errors_with_shot is False:
        placement = input("Enter a row and column to attack, like \"B5\":    ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement > 2):
            print("Error: Please enter only one row and column")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter a letter and then a number...")
            continue
        row = alphabet.find(row)
        if not (-1 < row < board_size):
            print("Error: Please enter a letter and then a number...")
            continue
        col = int(col)
        if not (-1 < col < board_size):
            print("Error: Please enter a letter and then a number...")
            continue
        if board[row][col] == "#" or board[row][col] == "X":
            print("You've already attacked this position...")
            continue
        if board[row][col] == "." or board[row][col] == "O":
            no_errors_with_shot = True
            
    return row, col        

def check_for_ship_sunk(row, col):
    
    global board
    global ship_positions
    
    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if board[r][c] != "X":
                        return False
    return True

def shoot_target():
    
    global board
    global num_ships_sunk
    global ammo
    
    row, col = accept_valid_bullet_placement()
    
    print("")
    print("_____________________________")
    
    if board[row][col] == ".":
        print("You missed, no ship was hit...")
        board[row][col] = "#"
    elif board[row][col] == "O":
        print("You hit!", end=" ")
        board[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("You completely sunk a ship!")
            num_ships_sunk += 1
        else:
            print("You shot a ship")
    
    ammo -= 1



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