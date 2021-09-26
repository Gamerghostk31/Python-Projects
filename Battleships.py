class Startup:
    def __init__(self) -> None:
        print("""             
  ____        _   _   _           _     _           
 |  _ \      | | | | | |         | |   (_)          
 | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ___ 
 |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|
 | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) \__ \
 |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/
                                         | |        
                                         |_|        
              by Basson Koch
             """ )

    def main_menu():
        menu_text = input("Press 1 to Start the game")
        print(menu_text)
        