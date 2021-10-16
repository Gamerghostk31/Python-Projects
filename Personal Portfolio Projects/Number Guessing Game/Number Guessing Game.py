# Number Guessing Game
# Author & Date: Basson Koch | 16/10/2021
# The player will start out with 100 points, after which the computer will prompt the player
# to select a difficulty. Normal (1 - 10) and Hard (1 - 100) the computer will then choose a a number in that range and if 
# the difficulty is set on hard it will give a clue. For every wrong guess, points are deducted. The aim is to guess the number before your score reaches 0
# The score will be saved in a text file and display the highest score for each difficulty on the next game. 

from random import randint, random
from datetime import time

score = 1000
game_over = False
user_input = ""


class number_generator():
    
    global random
    
    def __init__(self, game_difficulty):
        self.game_difficulty = game_difficulty
        

    def setGameDifficulty(self):
        
        random.seed(time.time())

        if self.game_difficulty == "hard":
            self.number = random.randint(1, 100)
            return self.number
        elif self.game_difficulty == "normal":
            self.number = random.randint(1, 10)
            return self.number

def check_game_over():
    
    global score
    global game_over

def user_move():
    pass

def check_number():
    pass

def edit_score():
    pass

def save_high_scores():
    pass

def main_menu():

    print("""
    WELCOME TO
                _   _  _     __            _ 
 |\ | | | |\/| |_) |_ |_)   /__  /\  |\/| |_ 
 | \| |_| |  | |_) |_ | \   \_| /--\ |  | |_ 
    BY BASSON KOCH
                                            
        """)
    
    
def select_difficulty():

    global user_input
    
    no_errors = False
    
    while no_errors is False:
        user_input = input("Select a difficulty!  Normal\/Hard  :    ")
        if user_input.isnumeric:
            print("Please type in letters, not numbers")
        elif user_input == None:
            print("Please type in \"normal\" or \"hard\"")
        elif user_input == "Normal" or user_input == "normal" or user_input == "NORMAL":
            user_input = user_input.lower()
            no_errors = True
        elif user_input == "Hard" or user_input == "hard" or user_input == "HARD":
            user_input = user_input.lower()
            no_errors = True
        else:
            print("Please type in \"normal\" or \"hard\"")
    


def main():
    
    global score
    global game_over
    global user_input
    
    main_menu()
    select_difficulty()
    number = number_generator(user_input)
    number.setGameDifficulty()

if __name__ == '__main__':
    main()