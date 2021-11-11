import random
from typing import no_type_check

class Game:

    def __init__(self):
        self.computerChoice = random.choice(["r", "p", "s"])
        self.score = 0
        self.compScore = 0
        self.userChoice = ""
        self.quit = False
        Game.game()
        

    def getUserInput():
        
        no_errors = False

        while no_errors == False:
            Game.userChoice = input("Enter your choice: (r for Rock / p for Paper / s for Scissors)             :")
            Game.userChoice.lower()
            if Game.userChoice == "r":
                print("You chose Rock!")
                no_errors = True
            elif Game.userChoice == "p":
                print("You chose Paper!")
                no_errors = True
            elif Game.userChoice == "s":
                print("You chose Scissors!")
                no_errors = True
            else:
                print("Please type in either: \"r\" \"p\" \"s\"")
                continue


    def checkAnswer():
        if Game.userChoice == Game.computerChoice:
            print (f"\n \nYou and the computer both choose {Game.userChoice}. \n It's a Tie!!")
            Game.score += 1
            Game.compScore += 1
        elif (Game.userChoice == "r" and Game.computerChoice == "s") or (Game.userChoice == "s" and Game.computerChoice == "p") or (Game.userChoice == "p" and Game.computerChoice == "r"):
            print (f"\n \nYou choose {Game.userChoice} over {Game.computerChoice} of computer. \n You Won The Round!!")
            Game.score += 1
        else:
            print (f"\n \nYou choose {Game.userChoice} but computer choose {Game.computerChoice} \n You Lost Sucker!!!")
            Game.compScore += 1

    def mainMenu():
        pass

    def playAgain():
        no_errors = False

        while no_errors is False:
            userAnswer = input("Play Again (Y/N)             :")
            userAnswer.lower()
            if userAnswer == "y":
                break
            elif userAnswer == "n":
                Game.quit = True
                break
            else:
                print("Please answer with (Y or N)")


    def checkWinner():
        if Game.score > Game.compScore:
            print(f"You beat the computer ({Game.score}:{Game.compScore:})")
        elif Game.score < Game.compScore:
            print(f"You lost to the computer ({Game.score}:{Game.compScore:})")
        else:
            print(f"The game ends in a tie ({Game.score}:{Game.compScore:})")

    def game():

        while Game.quit == False:
            Game.mainMenu()

            while Game.score != 3 and Game.compScore !=3:
                Game.getUserInput()
                Game.checkAnswer()
            
            Game.checkWinner()
            Game.playAgain()

            
game = Game()