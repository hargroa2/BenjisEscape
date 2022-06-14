#Story: You are Benji, a young but determined bearded dragon that was just adopted by a loving family. You came home in your kennel only to find out that the family’s 6 year old child named Timothy is your new owner. You have a strange feeling that Timothy doesn’t know how to take care of you and you fear that he may kill you! Use your wits to escape Timothy and his family’s home by defeating each of them in battle. It’s the only way to survive!

# FEATURES: REFERENCE

# 1. Benji will escape tank and have to fight Timothy first in his bedroom. Turn based match with health deduction by attacks

# 2. Story asks you what would you like to do next, you will run into mom in the dining room

# 3. Story asks you what you would like to do, living room with front door will lead to dad as final boss

# 4. If your health depletes to 0, it's game over and are taken back to the tank. If family member is at 0, they faint or cry/scream whatever

# 5. If you die you will be asked if you want to play again. If not, exit the program

# =====================================

import time
import textwrap
import sys
import os
import random

# screenWidth = 100

##### BENJI CLASS ###### COMMENT
class Benji:
    def __init__(self):
        self.health = 100
        self.attack = 20
        self.statusEffects = []
        self.gameOver = False

benji = Benji()

# class Timothy:
#     def __init__(self, health, attack):
#         self.health = health
#         self.attack = attack


# timothy = Timothy("50", "grab")
# print(timothy.health, timothy.attack)

###### PROMPT ######

def prompt():
    print("\n" + "==============================")
    print("     What would you like to do?")
    print("Please type one of the four options: ")

    print("         --   bite   --")
    print("         --   run    --")
    print("         --  scratch --")
    print("         --   quit   --")
    print("==============================")
    action = input("> ")
    moves = ['bite', 'run', 'scratch', 'quit']
    if action.lower() == 'bite':
        print("benjiBite(action.lower())")
        print("biting now")
    elif action.lower() == 'run':
        print("benjiRun(action.lower())")
        print("running now")
    elif action.lower() == 'scratch':
        print("benjiScratch(action.lower())")
        print("scratching now")
    elif action.lower() == 'quit':
        print("Quitting")
        sys.exit()
    while action.lower() not in moves:
        print("Unknown action, try again")
        action = input("> ")


###### GAME FUNCTIONALITY ######

def mainLoop():
    while benji.gameOver is False:
        prompt()

def setupGame():
    os.system('clear')
    # question1 = input("What's your name?\n")
    # for char in question1:
    #     sys.stdout.write(char)
    #     sys.stdout.flush()
    #     time.sleep(0.05)
    speech1 = "You are a young bearded dragon... \n"
    speech2 = "You escaped the tank. Your journey out of this dungeon of a home starts here.\n"
    speech3 = "Watch out for Timothy...\n"
    speech4 = "... And his family. \n"
    
    for char in speech1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    for char in speech2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    for char in speech3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    for char in speech4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

        # os.system('clear')
        mainLoop()

###### MENU LOGIC ###### COMMENT
def mainMenu():
    option = input("> ")
    if option.lower() == ("play"):
        setupGame()
    elif option.lower() == ("quit"):
        print("Quitting")
        sys.exit()
    while option.lower() not in ['play', 'quit']: #if command isn't play or quit, repeat
        print("Please enter a valid command: ")
        option = input("> ")
        if option.lower() == ("play"):
            setupGame()
        elif option.lower() == ("quit"):
            print("Quitting")
            sys.exit()

###### TITLE SCREEN VISUALS ######
def titleScreen():
    os.system('clear') # Moves screen up
    # print(chr(27) + "[2J") # This is for if your OS is not mac
    print("##############################")
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣢⣭⠓⣶⣶⣯⣽⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠿⠤⢯⣾⡿⢞⣫⣭⣍⢦⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢤⣦⣾⣯⣵⡾⢟⣫⣵⠾⠛⣉⣤⡌⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠠⣀⣤⣽⢰⣟⣵⠿⢛⣩⣤⣶⣿⣿⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠼⢿⣿⣿⣾⣭⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣤⣝⣛⡙⠛⠿⠻⣿⣿⣿⡿⣿⣿⡿⠛⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⢟⣠⣅⣀⣠⣴⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣶⣦⡈⠫⢍⣛⣿⣿⠿⠿⠿⠟⠋⠀⢀⣾⣿⣆⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣴⣿⣿⣿⣿⣶⣄⡈⠉⠉⠁⢀⣀⣀⣀⣴⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣴⣾⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣆⠀⠀⠀⠀
⣾⣿⣿⣿⣟⠉⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢈⣿⣿⣿⣿⡳⠦⢤⡀
⢻⣿⣿⣿⣿⣷⣦⣙⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⣸⢯⡿⠿⣮⡻⣄⠀⠈
⠀⠉⠙⠻⣿⠹⣿⢿⠙⣆⠙⠻⠿⠿⠛⠋⠉⠀⠀⠀⠀⣿⠘⡇⠀⠈⠳⡌⢣⠀
⠀⠀⠀⢀⠏⠀⢹⡎⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠐⠀⠀⠀⠰⠀⠁
⠀⠀⠀⠁⠀⠀⠀⠇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print('##############################')
    print("# Welcome to Benji's Escape! #")
    print('##############################')
    print('          .: Play :.          ')
    print('          .: Quit :.          ')
    print('    Copyright 2022 Amanda H.  ')
titleScreen()
mainMenu() # When you click play, it goes to the setupGame()
prompt()



titleScreen() #keep this at bottom














