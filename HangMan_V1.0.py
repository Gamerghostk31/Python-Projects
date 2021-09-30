import random
import time

wordlist = {1:"air conditioner", 2:"fighter jet", 3:"cheese pizza", 4:"pineapple", 5:"bacon and eggs"}


def pick_word():
    random.seed(time.time())
    word = wordlist[random.randint(1, len(wordlist))]
    new_word = word.replace(" ", "")
    print(new_word)
    pass

def get_input():
    pass

def check_word():
    pass

def draw_picture():
    pass

def check_game_over():
    pass

def main():
    pick_word()
    pass

if __name__ == '__main__':
    main()
    