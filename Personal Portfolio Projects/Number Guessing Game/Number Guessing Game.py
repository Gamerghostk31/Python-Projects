# Number Guessing Game
# Author & Date: Basson Koch | 16/10/2021

# IMPORTANT!!!!
# To run the game correctly, make sure the terminal is in the directory of the .py and json files.

# PLEASE_NOTE!!!
# Turn Dev Mode off to experience true "HARD MODE" (Normal mode is always easy)

dev_mode = True

# The computer will pick a number from (1 - 10 / Normal) or (1 - 100 / Hard). 
# The player will gain points for how close your guess is to the correct number.
# Closer means more points, further less points. After you guess the number, your remaining turns will act as bonus points. 
# Solve the number faster for a higher score.
# If you have the highest score. You will become the CHAMPION!

import random
import time
import json

score = 0
game_over = False
user_input = None
user_guess = 0
random_number = 0
user_win = False
user_guesses = []
exit = False

class number_generator():
    
    global random
    global time
    
    def __init__(self, game_difficulty):
        self.game_difficulty = game_difficulty
        print("_____________________________________________")
        print(f"\nYou chose {self.game_difficulty} mode!\n")
        

    def setGameDifficulty(self):
        
        random.seed(time.time())

        if self.game_difficulty == "hard":
            self.number = random.randint(1, 100)
            self.turns = 10
            return self.number
        elif self.game_difficulty == "normal":
            self.number = random.randint(1, 10)
            self.turns = 5
            return self.number

def check_game_over():
    
    global score
    global game_over
    global user_win
    global random_number

    if number.turns == 0 and user_win == False:
        
        print("""\n
  __            _    _        _  _  
 /__  /\  |\/| |_   / \ \  / |_ |_) 
 \_| /--\ |  | |_   \_/  \/  |_ | \ 
                                    
        """)
        
        print(f"The correct number was:   {random_number}")
        print("\nYour score is:   " + str(score))
        
        game_over = True
    elif user_win == True:
        if number.game_difficulty == "hard":
            score = score + (number.turns * 100)
            
            print("""\n
      _              ___      
 \_/ / \ | |   \    / |  |\ | 
  |  \_/ |_|    \/\/ _|_ | \| 
                              
            """)
            
            print("Your score is:  " + str(score) + "\n")
            
            game_over = True
        elif number.game_difficulty == "normal":
            score = score + (number.turns * 10)
            
            print("""\n
      _              ___      
 \_/ / \ | |   \    / |  |\ | 
  |  \_/ |_|    \/\/ _|_ | \| 
                              
            """)
            
            print("Your score is:  " + str(score) + "\n")
            
            game_over = True

def user_move():
    
    global user_guess
    global score

    no_errors = False

    guess_string = ""
    print("_____________________________________________")
    print(f"\nTurns Left: {number.turns}")
    print("Total Score:   " + str(score)+"\n")
    print("_____________________________________________")

    if len(user_guesses) == 0:
        pass
    else:
        user_guesses.sort()
        for i in range(len(user_guesses)):
            guess_string += " " + str(user_guesses[i]) + " "
            
        print(f"\nYou've already guessed the numbers: {guess_string}\n")
        

    while no_errors is False:
        num_range = None
        if number.game_difficulty == "normal":
            num_range = "1 - 10"
        elif number.game_difficulty == "hard":
            num_range = "1 - 100"

        
        user_guess = input("\nGuess any number from " + num_range + "\n:     ")
        
        if user_guess.isalpha():
            print("_____________________________________________")
            print("ERROR: please type in a number!")
            print("_____________________________________________")
        elif len(user_guess) > 1 and number.game_difficulty == "normal":
            print("_____________________________________________")
            print("ERROR: Please pick a number from " + num_range)
            print("_____________________________________________")
        elif len(user_guess) > 2 and number.game_difficulty == "hard":
            print("_____________________________________________")
            print("ERROR: Please pick a number from " + num_range)
            print("_____________________________________________")
        elif user_guess in user_guesses:
            print("_____________________________________________")
            print("ERROR: You can't guess the same number twice\n \n-1 TURN AS PENALTY")
            number.turns -= 1
            print("_____________________________________________")
        else:
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("_____________________________________________\n")
            print("YOUR GUESS: " + str(user_guess)+ "\n")

            user_guesses.append(user_guess)

            number.turns -= 1
            
            no_errors = True

def check_number():
    
    global user_guess
    global random_number
    global score
    global user_win

    difference = random_number - int(user_guess)
    
    if number.game_difficulty == "hard":
        
        if random_number == int(user_guess):
            score += 100
            print('You guessed the number! Well Done!')
            user_win = True

        elif difference >= 1 and difference <= 5 or difference <= 1  and difference >= -5:
            score += 35
            print("SOOOO CLOSE! \nYou gained 35 points")

        elif difference > 5 and difference <= 10 or difference < 5 and difference >= -10:
            score += 30
            print("CLOSE! \nYou gained 30 points")

        elif difference > 10 and difference <= 20 or difference < -10 and difference >= -20:
            score += 20
            print("Almost, \nYou gained 20 points")
            
        elif difference > 20 and difference <= 30 or difference < -20 and difference >= -30:
            score += 10
            print("Not quite, \nYou gained 10 points")
            
        
        else:
            score += 0
            print("Ouch! That guess was too far away. \nYou gained 0 points")
            
    
    elif number.game_difficulty == "normal":
        
        if random_number == int(user_guess):
            score += 10
            print('You guessed the number! Well Done!')
            
            user_win = True
        
        elif difference == 1 or difference == -1:
            score += 3
            print("CLOSE! \nYou gained 3 points")
            
        elif difference == 2 or difference == -2:
            score += 2
            print("Almost, \nYou gained 2 points")
            
        elif difference == 3 or difference == -3:
            score += 1
            print("Not quite, \nYou gained 1 point")
        
        else:
            score += 0
            print("Ouch! That guess was too far away. \nYou gained 0 points")

def print_current_high_score():

    mode = number.game_difficulty
    current_champ = ""
    current_high = 0
    champ_mode = 0

    if mode == "normal":
        with open("high_score_normal.json", "r") as scoresheet:
            score_data = json.load(scoresheet)
            if score_data["mode"] == mode:
                current_champ = score_data["username"]
                current_high = score_data["high_score"]
                champ_mode = score_data["mode"]

    elif mode == "hard":
        with open("high_score_hard.json", "r") as scoresheet:
            score_data = json.load(scoresheet)
            if score_data["mode"] == mode:
                current_champ = score_data["username"]
                current_high = score_data["high_score"]
                champ_mode = score_data["mode"]

    print("_____________________________________________")
    print(f"The current champion is {current_champ} \nwith a score of {current_high} in {champ_mode} mode.")
    print("_____________________________________________")

def save_high_scores():

    global score

    
    no_errors = False
    while no_errors is False:
        username = input("Please write your username  \n:         ")
        no_confirm_errors = False
        while no_confirm_errors is False:
        
            confirm = input(f"Are you sure you want {username} as your username? (Y/N)\n:    ")
            confirm = confirm.upper()

            if confirm == "Y":
                no_confirm_errors = True
                no_errors = True
            elif confirm == "N":
                no_errors = False
                no_confirm_errors = True
            else:
                print("_____________________________________________")
                print("ERROR:  Please type \"Y\" or \"N\" to confirm your username...")
                print("_____________________________________________")
    
    turn_to_json = {'username':username, "high_score":score, "mode":number.game_difficulty}

    mode = number.game_difficulty
    higher_score = False

    if mode == "normal":
        with open("high_score_normal.json") as data_file:
            data = json.load(data_file)
            if data["high_score"] < turn_to_json["high_score"]:
                    del data["username"]
                    del data["high_score"]
                    del data["mode"]
                    print("You are the new Champion!")
                    higher_score = True
            else:
                print("You did not defeat the Champion!")
                
        if higher_score:
            with open("high_score_normal.json", "w") as json_data:
                json.dump(turn_to_json, json_data)

    elif mode == "hard":
        with open("high_score_hard.json") as data_file:
            data = json.load(data_file)
            if data["high_score"] < turn_to_json["high_score"]:
                    del data["username"]
                    del data["high_score"]
                    del data["mode"]
                    print("You are the new Champion!")
                    higher_score = True
            else:
                print("You did not defeat the Champion!")
                
        if higher_score:
            with open("high_score_hard.json", "w") as json_data:
                json.dump(turn_to_json, json_data)
    
    print("High score saved...")
        
def play_again():

    global exit

    again = input("Play again?      Type (Y/N) \n:         ")
    again = again.upper()
    no_error = False
    while no_error is False:
        if again == "Y":
            exit = False
            no_error = True
        elif again == "N":
            exit = True
            no_error = True
        else:
            print("_____________________________________________")
            print("ERROR:  Please type \"Y\" or \"N\"")
            print("_____________________________________________")

def main_menu():
    print("""
______________________________________________________________________________________________
                                    WELCOME TO
                                   _   _  _     __            _ 
                    |\ | | | |\/| |_) |_ |_)   /__  /\  |\/| |_ 
                    | \| |_| |  | |_) |_ | \   \_| /--\ |  | |_ 
    
                                  BY BASSON KOCH
______________________________________________________________________________________________                                            
        The computer will pick a number from (1 - 10 / Normal) or (1 - 100 / Hard). 

        The player will gain points for how close the guess is to the correct number.

                        Closer means more points, further less points. 
        
        After you guess the number, your remaining turns will act as bonus points. 
        
                        Solve the number faster for a higher score.
    
                If you have the highest score. You will become the CHAMPION!  

                                    GOODLUCK player    
______________________________________________________________________________________________        
        """)   
    
def select_difficulty():

    global user_input
    
    no_errors = False
    
    while no_errors is False:
        user_input = input("Select a difficulty!  Normal/Hard  :    ")
        if user_input == None:
            print("_____________________________________________")
            print("ERROR:  Please type in \"normal\" or \"hard\"")
            print("_____________________________________________")
        elif user_input == "Normal" or user_input == "normal" or user_input == "NORMAL":
            user_input = user_input.lower()
            no_errors = True
        elif user_input == "Hard" or user_input == "hard" or user_input == "HARD":
            user_input = user_input.lower()
            no_errors = True
        else:
            print("_____________________________________________")
            print("ERROR:  Please type in \"normal\" or \"hard\"")
            print("_____________________________________________")
    
def main():
    
    
    global number
    global score
    global game_over
    global user_input
    global random_number
    global dev_mode
    global total_score
    global user_guesses
    
    
    while exit == False:
        
        if game_over:
            game_over = False
            total_score = 0
            user_guesses = []

        
        main_menu()

        select_difficulty()

        number = number_generator(user_input)
        random_number = number.setGameDifficulty()

        print_current_high_score()
    
        while game_over == False:
            if dev_mode == True:
                print(random_number)
            user_move()
            print("_____________________________________________")
            check_number()
            print("_____________________________________________")
            check_game_over()
        
        save_high_scores()
        play_again()
    
    
    exit()

if __name__ == '__main__':
    main()