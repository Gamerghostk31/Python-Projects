import random

def game():
  
  while True:
    user = input("Enter your choice : \n (r for Rock, p for Paper, s for Scissor) || r/p/s => ")
    user = user.lower()
    if user =="r" or user == "p" or user == "s":
      break
    else:
      print("\n \n Read the instruction and give the correct input you mf!\n \n")
      continue

  computer = random.choice(["r", "p", "s"])
  
  if user == computer:
    print (f"\n \nYou and the computer both choose {user}. \n It's a Tie!!")

  elif (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
    print (f"\n \nYou choose {user} over {computer} of computer. \n You Won!!")
  
  else:
    print (f"\n \nYou choose {user} but computer choose {computer} \n You Lost Sucker!!!")

while True:
  game()
  play_again = input("\n \nWanna play again bitch! y/n? :")
  if play_again.lower()== "y":
    continue
  elif play_again.lower()== "n":
    print ("\n \nSee ya later scared bitch!")
    break
  else:
    print("\n \nYou suck at reading instruction! \n Get lost!")
    break