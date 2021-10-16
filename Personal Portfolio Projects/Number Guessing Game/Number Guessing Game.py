# Number Guessing Game
# Author & Date: Basson Koch | 16/10/2021
# The player will start out with 100 points, after which the computer will prompt the player
# to select a difficulty. Normal (1 - 10) and Hard (1 - 100) the computer will then choose a a number in that range and if 
# the difficulty is set on hard it will give a clue. For every wrong guess, points are deducted. The aim is to guess the number before your score reaches 0
# The score will be saved in a text file and display the highest score for each difficulty on the next game. 

from random import randint, random
from datetime import time



class number_generator():
    
    global random
    
    def __init__(self, game_difficulty):
        self.game_difficulty = game_difficulty

    def setGameDifficulty(self):
        
        if self.game_difficulty == "hard":
            self.number = random.randint(1, 100)
            return self.number
        elif self.game_difficulty == "normal":
            self.number = random.randint(1, 10)
            return self.number

def check_game_over():
    pass

def main():
    pass

if __name__ == '__main__':
    main()