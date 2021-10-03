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
    
def print_grid():

    global grid
    global alphabet
    
    alphabet = alphabet[0: len(grid) + 1]
    
    for row in range(len(grid)):
        print(alphabet[row], end=")  ")
        for col in range(len(grid[row])):
            if grid[row][col] == "X":
                pass
            elif grid[row][col] == "#":
                pass
            else:
                print(".", end=" ")
        print("")
    
    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")
    
    
    

def check_ships_in_range():
    pass

def check_ship_collision():
    pass

def shoot():
    pass

def check_ship_hit():
    pass

def check_game_over():
    pass

# Main Method
def main():
    create_grid()
    print_grid()

if __name__ == '__main__':
    main()