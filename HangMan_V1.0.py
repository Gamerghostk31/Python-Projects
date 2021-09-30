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
    
    if guess in word:
        letters_used += guess
        word1 = word.replace(guess, "")
        word = word1
        update_score()
    else:
        incorrect_letters += guess
        draw_picture()

def draw_picture():
    
    global mistakes
    
    mistakes += 1
    
    if mistakes == 1:
        print("""
                      shhhhhhhhhhhhhhhhhhhhhhhhs             
          `NN/////oNMd/////////////NN`            
          `NN`  .sNd:`                     
          `NN`.oNd/`                        
          `NNomm+`                    
          `NMm+`                     
          `NN.                     
          `NN`                    
          `NN`                     
          `NN`                     
          `NN`                    
          `NN`                       
          `NN`                           
          `NN`                   
          `NN`              
          `NN`               
          `NN`                             
          `NN`                            
          `NN`                            
          `NN`                          
          `NN`                       
          `NN`                   
     -/////NN/////-                
     shhhhhhhhhhhhs                         
              """)
    elif mistakes == 2:
        print("""
                      shhhhhhhhhhhhhhhhhhhhhhhhs             
          `NN/////oNMd/////////////NN`            
          `NN`  .sNd:`            `NN`            
          `NN`.oNd/`              `NN`            
          `NNomm+`                `NN`            
          `NMm+`                     
          `NN.                      
          `NN`                    
          `NN`               
          `NN`                   
          `NN`                        
          `NN`                            
          `NN`                             
          `NN`                     
          `NN`                 
          `NN`              
          `NN`                            
          `NN`                              
          `NN`                          
          `NN`                           
          `NN`                      
          `NN`                      
     -/////NN/////-                 
     shhhhhhhhhhhhs                         
              """)
    elif mistakes == 3:
        print("""
                      shhhhhhhhhhhhhhhhhhhhhhhhs             
          `NN/////oNMd/////////////NN`            
          `NN`  .sNd:`            `NN`            
          `NN`.oNd/`              `NN`            
          `NNomm+`                `NN`            
          `NMm+`                `-+NN+-`          
          `NN.                 +dmhsshmd+         
          `NN`                oMy.    .yMo        
          `NN`                NM`      `MN        
          `NN`                hM+      +Mh        
          `NN`                `yNh+::+hNy`        
          `NN`                  .+yMMy+.          
          `NN`                             
          `NN`                     
          `NN`                 
          `NN`              
          `NN`                            
          `NN`                              
          `NN`                          
          `NN`                           
          `NN`                      
          `NN`                      
     -/////NN/////-                 
     shhhhhhhhhhhhs                         
              """)
    elif mistakes == 4:
        print("""
                      shhhhhhhhhhhhhhhhhhhhhhhhs             
          `NN/////oNMd/////////////NN`            
          `NN`  .sNd:`            `NN`            
          `NN`.oNd/`              `NN`            
          `NNomm+`                `NN`            
          `NMm+`                `-+NN+-`          
          `NN.                 +dmhsshmd+         
          `NN`                oMy.    .yMo        
          `NN`                NM`      `MN        
          `NN`                hM+      +Mh        
          `NN`                `yNh+::+hNy`        
          `NN`                  .+yMMy+.          
          `NN`                    `NN`            
          `NN`               `-/sdNMMNds/-`       
          `NN`             odNdho/-NN-/ohdNdo     
          `NN`             ::.`            `.::     
          `NN`                               
          `NN`                           
          `NN`                              
          `NN`                           
          `NN`                        
          `NN`                       
     -/////NN/////-                   
     shhhhhhhhhhhhs                         
              """)
    elif  mistakes == 5:
        print("""
                      shhhhhhhhhhhhhhhhhhhhhhhhs             
          `NN/////oNMd/////////////NN`            
          `NN`  .sNd:`            `NN`            
          `NN`.oNd/`              `NN`            
          `NNomm+`                `NN`            
          `NMm+`                `-+NN+-`          
          `NN.                 +dmhsshmd+         
          `NN`                oMy.    .yMo        
          `NN`                NM`      `MN        
          `NN`                hM+      +Mh        
          `NN`                `yNh+::+hNy`        
          `NN`                  .+yMMy+.          
          `NN`                    `NN`            
          `NN`               `-/sdNMMNds/-`       
          `NN`             odNdho/-NN-/ohdNdo     
          `NN`             ::.`   `NN`   `.::     
          `NN`                    `NN`            
          `NN`                    `NN`            
          `NN`                   `/MM/`           
          `NN`                            
          `NN`                       
          `NN`                      
     -/////NN/////-                  
     shhhhhhhhhhhhs                         
              """)
    elif mistakes == 6:
        print("""
                      shhhhhhhhhhhhhhhhhhhhhhhhs             
          `NN/////oNMd/////////////NN`            
          `NN`  .sNd:`            `NN`            
          `NN`.oNd/`              `NN`            
          `NNomm+`                `NN`            
          `NMm+`                `-+NN+-`          
          `NN.                 +dmhsshmd+         
          `NN`                oMy.    .yMo        
          `NN`                NM`      `MN        
          `NN`                hM+      +Mh        
          `NN`                `yNh+::+hNy`        
          `NN`                  .+yMMy+.          
          `NN`                    `NN`            
          `NN`               `-/sdNMMNds/-`       
          `NN`             odNdho/-NN-/ohdNdo     
          `NN`             ::.`   `NN`   `.::     
          `NN`                    `NN`            
          `NN`                    `NN`            
          `NN`                   `/MM/`           
          `NN`                  -hNssNh-          
          `NN`                `oNd:  :dNo`        
          `NN`                yNo`    `oNh        
     -/////NN/////-           `.        ..        
     shhhhhhhhhhhhs                         
              """)

def update_score():
    
    global score
    global word
    global letters_used
    global incorrect_letters
    
    score = len(word)
    
    print("____________________________________________________________________")
    print("Good Job! You have {score} letters left to go!".format(score=score))
    print("You've already used: {letters} which are correct ".format(letters=letters_used))
    print("You've already used: {inletters} which are incorrect ".format(inletters=incorrect_letters))
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
    