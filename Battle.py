from random import randint

# Global variables
board = []
board_size = 0
num_of_ships = 0
ships_sunk = 0
bullets = 0
win_lose = False
game_over = False
ships = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
difficulty = "easy"

def game_start():
    print("""
          Welcome to....
            BATTLESHIPS!!!
            by Basson Koch
    ____________________________
          """)
    difficulty_setting()

def difficulty_setting():
    difficulty = input("Choose your difficulty: \'easy\' \'normal\' \'hard\':   ")
    if difficulty == "easy":
        board_size = 5
        num_of_ships = 3
        bullets = 30
        create_board(board_size)
        create_ships(num_of_ships)
        print_board(board)
    elif difficulty == "normal":
        board_size = 10
        num_of_ships = 8
        bullets = 50
        create_board(board_size)
        create_ships(num_of_ships)
        print_board(board)
    elif difficulty == "hard":
        board_size = 12
        num_of_ships = 12
        bullets = 50
        create_board(board_size)
        create_ships(num_of_ships)
        print_board(board)
    else:
        print("Please choose a valid difficulty setting...")
        difficulty_setting()
        
def create_board(board_size):
    board = [[c]+['.' for _ in range(board_size)] for c in alphabet(0, board_size)]
    board.append([' ']+[x for x in range(board)])


def create_ships(num_of_ships):
    pass

def print_board(board):
    for r in alphabet(0, board_size):
        print(r) *board_size










def main():
    game_start()
    while game_over != True:
        pass
    
    if win_lose == True:
        print("You WON!")
        again = input("Try again? 'Y' or 'N':    ")
        if again == 'Y':
            game_over = False
            main()
        elif again == 'N':
            exit
        else:
            exit
    else:
        print("You lost...")
        again = input("Try again? 'Y' or 'N':    ")
        if again == 'Y':
            game_over = False
            main()
        elif again == 'N':
            exit
        else:
            exit

main()