# Modules Needed
import random
import time

# Global Variables Needed
grid = []
grid_size = 10
num_of_ships = 8
ships_sunk = 0
ship_positions = []
ammo = 50
game_over = False
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Methods Needed
def create_grid():
    
    global grid
    global grid_size
    
    rows, cols = (grid_size, grid_size)
    
    for row in range(rows):
        row_list = []
        for col in range(cols):
            row_list.append(".")
        grid.append(row_list)
              
def create_ship_positions():
    
    random.seed(time.time())
    
    global grid
    global grid_size
    global num_of_ships
    global ship_positions
    
    rows, cols = (grid_size, grid_size)
    
    ships_placed = 0
    
    while ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        random_size = random.randint(2, 5)
        if check_ships_in_range(random_row, random_col, direction, random_size):
            ships_placed += 1
    
def print_grid():

    global grid
    global alphabet
    
    alphabet = alphabet[0: len(grid) + 1]
    
    debug_mode = True
    
    for row in range(len(grid)):
        print(alphabet[row], end=")  ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")
    
    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")
          
def check_ships_in_range(row, col, direction, size):
    
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - size < 0:
            return False
        start_col = col - size + 1

    elif direction == "right":
        if col + size >= grid_size:
            return False
        end_col = col + size

    elif direction == "up":
        if row - size < 0:
            return False
        start_row = row - size + 1

    elif direction == "down":
        if row + size >= grid_size:
            return False
        end_row = row + size

    return add_ships(start_row, end_row, start_col, end_col)

def add_ships(start_row, end_row, start_col, end_col):
    
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid

def shoot():
    
    global grid
    global ships_sunk
    global ammo
    
    row, col = bullet_placement()
    
    print("")
    print("_____________________________")
    
    if grid[row][col] == ".":
        print("You missed, no ship was hit...")
        grid[row][col] = "#"
    elif grid[row][col] == "O":
        print("You hit!", end=" ")
        grid[row][col] = "X"
        if check_ship_hit(row, col):
            print("You completely sunk a ship!")
            ships_sunk += 1
        else:
            print("You shot a ship")
    
    ammo -= 1

def bullet_placement():
    global alphabet
    global grid
    
    no_errors_with_shot = False
    row = -1
    col = -1
    while no_errors_with_shot is False:
        placement = input("Enter a row and column to attack, like \"B5\":    ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter only one row and column")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter a letter and then a number...")
            continue
        row = alphabet.find(row)
        if not (-1 < row < grid_size):
            print("Error: Please enter a letter and then a number...")
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print("Error: Please enter a letter and then a number...")
            continue
        if grid[row][col] == "#" or grid[row][col] == "X":
            print("You've already attacked this position...")
            continue
        if grid[row][col] == "." or grid[row][col] == "O":
            no_errors_with_shot = True
            
    return row, col   

def check_ship_hit(row, col):
    global grid
    global ship_positions
    
    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != "X":
                        return False
    return True

def check_game_over():
    
    global game_over
    global ammo
    global num_of_ships
    global ships_sunk
    
    if num_of_ships == ships_sunk:
        print("YOU WIN! CONGRATULATIONS!!!")
        game_over = True
    elif  ammo <= 0:
        print("Sorry, you're out of ammo... GAME OVER")
        game_over = True

# Main Method
def main():
    
    global game_over
    global num_of_ships
    global ships_sunk
    global ammo
    
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
    
    create_grid()
    create_ship_positions()
    
    while game_over is False:
        print_grid()
        print("There are {ships} ships remaining, You have sunk {ships_sunk} ships".format(ships=num_of_ships, ships_sunk=num_ships_sunk))
        print("You have {ammo} rounds of ammo remaining".format(ammo=ammo))
        shoot()
        print("________________________________")
        print("")
        check_game_over()

if __name__ == '__main__':
    main()