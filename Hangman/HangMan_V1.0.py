import random
import time

wordlist = {1:"air conditioner", 2:"fighter jet", 3:"cheese pizza", 4:"pineapple", 5:"bacon and eggs", 6:"television", 7:"amberella", 8:"brocolli", 9:"cauliflower", 10:"casava root"}

word = ""
guess = ""
score = ""
mistakes = 0
game_over = False
letters_used = ""
incorrect_letters = ""
original_word = ""
letters = []

def pick_word():
    
    global wordlist
    global word
    global score
    global original_word
    global letters
    
    random.seed(time.time())
    word = wordlist[random.randint(1, len(wordlist))]
    original_word = word.replace(" ", "")
    word = word.replace(" ", "")
    
    score = len(word)
    
    letters = ["_" for letter in original_word]

def get_input():
    
    global guess
    
    no_errors = False
    
    while no_errors is False:
        print("____________________________________________________________________")
        guess = input("Type in any letter from A-Z:      ")
        print("____________________________________________________________________\n")
        guess.lower()
        if (len(guess) <= 0 or len(guess) >= 2) or guess.isnumeric():
            print("please type only one letter for your guess...\n")
            continue
        else:
            no_errors = True              

def check_word():
    
    global guess
    global word
    global letters_used
    global incorrect_letters
    global mistakes
    global original_word
    global letters
    
    letters_used = ""
    
    no_errors = False
    while no_errors is False:
        
        if guess in word:
            for i in range(len(original_word)):
                if original_word[i] == guess:
                    letters[i] = guess
        
            for element in letters:
                letters_used += str(element)
            
            word1 = word.replace(guess, "")
            word = word1
            print("\n                   WELL DONE")
            
            if mistakes >= 1:
                draw_picture()
            update_score()
            
            no_errors = True
        
        else:
            for element in letters:
                letters_used += str(element)
                
            error_here = False
            for i in range(len(letters)):
                if letters[i] == guess:
                    print("\n           You've already guessed that letter")
                    error_here = True
                    break
            
            if error_here is True:
                draw_picture()
                update_score()
                no_errors = True
                break
            else:
            
                mistakes += 1
                print("\n           Oh no, that's an incorrect guess...")
                incorrect_letters += guess
            
                draw_picture()
                update_score()
                no_errors = True         

def draw_picture():
    
    global mistakes
    
    
    if mistakes == 1:
        print("""
    `---------------        
      /m//+md//////      
      /d`od:                
      /Nd:               
      /d            
      /d              
      /d               
      /d               
      /d         
      /d         
      /d                
      /d                
      /d             
   ://sm///`        
   --------`                           
              """)
    elif mistakes == 2:
        print("""
     `---------------        
      /m//+md////////M-       
      /d`od:         N-       
      /Nd:           M-       
      /d            
      /d              
      /d               
      /d               
      /d         
      /d         
      /d                
      /d                
      /d             
   ://sm///`        
   --------`                                    
              """)
    elif mistakes == 3:
        print("""
    `---------------        
      /m//+md////////M-       
      /d`od:         N-       
      /Nd:          .M:       
      /d          /do/+do     
      /d          N:   `M.    
      /d          +d/:/hs     
      /d           `:M+`      
      /d           
      /d        
      /d                  
      /d                
      /d             
   ://sm///`        
   --------`                              
              """)
    elif mistakes == 4:
        print("""
    `---------------        
      /m//+md////////M-       
      /d`od:         N-       
      /Nd:          .M:       
      /d          /do/+do     
      /d          N:   `M.    
      /d          +d/:/hs     
      /d           `:M+`      
      /d        `:oyyMhyo/.   
      /d        :/.      .:/   
      /d                  
      /d                
      /d             
   ://sm///`        
   --------`                              
              """)
    elif  mistakes == 5:
        print("""
    `---------------        
      /m//+md////////M-       
      /d`od:         N-       
      /Nd:          .M:       
      /d          /do/+do     
      /d          N:   `M.    
      /d          +d/:/hs     
      /d           `:M+`      
      /d        `:oyyMhyo/.   
      /d        :/.  N- .:/   
      /d             N-       
      /d                
      /d             
   ://sm///`        
   --------`                              
              """)
    elif mistakes == 6:
        print("""
    `---------------        
      /m//+md////////M-       
      /d`od:         N-       
      /Nd:          .M:       
      /d          /do/+do     
      /d          N:   `M.    
      /d          +d/:/hs     
      /d           `:M+`      
      /d        `:oyyMhyo/.   
      /d        :/.  N- .:/   
      /d             N-       
      /d           `smh.      
      /d          /d/ :do     
   ://sm///`      :`    :`    
   --------`                              
              """)

def update_score():
    
    global score
    global word
    global letters_used
    global incorrect_letters
    
    score = len(word)
    
    print("____________________________________________________________________")
    print("You have {score} letters left to go!".format(score=score))
    print("Correct: {letters}".format(letters=letters_used))
    print("Incorect: {inletters}".format(inletters=incorrect_letters))
    print("____________________________________________________________________")

def check_game_over():
    
    global game_over
    global mistakes
    global word
    
    if len(word) == 0:
        print("################################################")
        print("""
      _              ___        
 \_/ / \ | |   \    / |  |\ | | 
  |  \_/ |_|    \/\/ _|_ | \| o 
                           __  _                                              
 \_/ _         _. ._ _    (_  |_ \/ \_/ | | | 
  | (_) |_|   (_| | (/_   __) |_ /\  |  o o o 
                                               
                                                                               
              """)
        print("################################################")
        game_over = True
    
    if mistakes == 6:
        print("################################################")
        print("""
      _            _   __ ___      
 \_/ / \ | |   |  / \ (_   |       
  |  \_/ |_|   |_ \_/ __)  | o o o 
  
                                          __  _              
 \_/ _         _. ._ _     _ _|_ o | |   (_  |_ \/ \_/ | | | 
  | (_) |_|   (_| | (/_   _>  |_ | | |   __) |_ /\  |  o o o 
                                                             
  __            _    _        _  _  
 /__  /\  |\/| |_   / \ \  / |_ |_) 
 \_| /--\ |  | |_   \_/  \/  |_ | \                                   
                               
              """)
        print("################################################")
        game_over = True

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
    