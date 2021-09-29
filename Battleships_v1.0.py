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
    
    
    

if __name__ == '__main__':
    main()