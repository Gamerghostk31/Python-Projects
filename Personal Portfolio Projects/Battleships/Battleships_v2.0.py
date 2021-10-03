# Modules Needed
import random
import time

# Global Variables Needed
grid = []
grid_size = 10
num_of_ships = 8
ships_sunk = 0
ship_positions = []
ammo = 0
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
    pass

def check_ship_hit():
    pass

def check_game_over():
    pass

# Main Method
def main():
    create_grid()
    create_ship_positions()
    print_grid()

if __name__ == '__main__':
    main()