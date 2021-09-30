import random
import time

wordlist = {1:"air conditioner", 2:"fighter jet", 3:"cheese pizza", 4:"pineapple", 5:"bacon and eggs"}

word = ""
guess = ""
score = ""
mistakes = 0
game_over = False

def pick_word():
    
    global wordlist
    global word
    global score
    
    random.seed(time.time())
    word = wordlist[random.randint(1, len(wordlist))]
    word = word.replace(" ", "")
    
    score = len(word)
    
    print(word)
    print(score)

def get_input():
    
    global guess
    
    no_errors = False
    
    while no_errors is False:
        guess = input("Type in any letter from A-Z:      ")
        guess.lower()
        if (len(guess) <= 0 or len(guess) >= 2) or guess.isnumeric():
            print("please type only one letter for your guess")
            continue
        else:
            no_errors = True              

def check_word():
    
    global guess
    global word
    
    if guess in word:
        word.remove(guess)
        update_score()
    else:
        draw_picture()

def draw_picture():
    
    global mistakes
    
    mistakes += 1
    
    if mistakes == 1:
        print("Wrong...")
    elif mistakes == 2:
        print("Wrong...")
    elif mistakes == 3:
        print("Wrong...")
    elif mistakes == 4:
        print("Wrong...")
    elif  mistakes == 5:
        print("Wrong...")
    elif mistakes == 6:
        print("Wrong...")

def update_score():
    
    global score
    global word
    
    score = len(word)
    
    print("Good Job! You have {score} letters left to go!".format(score=score))

def check_game_over():
    
    global game_over
    global mistakes
    global word
    
    if len(word) == 0:
        print("You WIN!!!")
        game_over = True
    
    if mistakes == 6:
        print("You lost...")
        game_over = True
    
    if game_over:
        print("Game over")

def main():
    
    global game_over
    
    print("""
                   WELCOME to
        _____________________________                                      
        |_|  _. ._   _  ._ _   _. ._  
        | | (_| | | (_| | | | (_| | | 
                     _|              
        _____________________________
                By Basson Koch
          """)
    
    pick_word()
    
    while game_over is False:
        get_input()
        check_word()
        check_game_over()
    
if __name__ == '__main__':
    main()
    