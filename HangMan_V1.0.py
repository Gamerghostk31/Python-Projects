import random
import time

wordlist = {1:"air conditioner", 2:"fighter jet", 3:"cheese pizza", 4:"pineapple", 5:"bacon and eggs"}

word = ""
guess = ""
score = ""
mistakes = 0
game_over = False
letters_used = ""
incorrect_letters = ""

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
        print("____________________________________________________________________")
        guess = input("Type in any letter from A-Z:      ")
        print("____________________________________________________________________")
        guess.lower()
        if (len(guess) <= 0 or len(guess) >= 2) or guess.isnumeric():
            print("please type only one letter for your guess...")
            continue
        else:
            no_errors = True              

def check_word():
    
    global guess
    global word
    global letters_used
    global incorrect_letters
    global mistakes
    
    if guess in word:
        letters_used += guess
        word1 = word.replace(guess, "")
        word = word1
        if mistakes > 1:
            draw_picture()
        update_score()
    else:
        print("Oh no, that's an incorrect guess...")
        incorrect_letters += guess
        draw_picture()
        update_score()

def draw_picture():
    
    global mistakes
    
    mistakes += 1
    
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
                               
              """)
        print("################################################")
        game_over = True
    
    if mistakes == 6:
        print("################################################")
        print("""
                         _            _   __ ___      
                    \_/ / \ | |   |  / \ (_   |       
                     |  \_/ |_|   |_ \_/ __)  | o o o 
                                    
                               
              """)
        print("################################################")
        game_over = True
    
    if game_over:
        print(""" 
                 __            _    _        _  _  
                /__  /\  |\/| |_   / \ \  / |_ |_) 
                \_| /--\ |  | |_   \_/  \/  |_ | \ 
   
              """)

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
    