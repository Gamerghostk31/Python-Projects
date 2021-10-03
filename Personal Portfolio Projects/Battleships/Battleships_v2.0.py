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

# Methods Needed
def create_grid():
    
    global grid
    global grid_size
    
    rows, cols = grid_size, grid_size
    
    for row in rows:
        row_list = []
        for col in cols:
            row_list.append(".")
        grid.append(row_list)
            
    

def create_ship_positions():
    pass

def print_grid():
    pass

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
    pass

if __name__ == '__main__':
    main()