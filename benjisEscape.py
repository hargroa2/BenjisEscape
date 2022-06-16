#Story: You are Benji, a young but determined bearded dragon that was just adopted by a loving family. You came home in your kennel only to find out that the family’s 6 year old child named Timothy is your new owner. You have a strange feeling that Timothy doesn’t know how to take care of you and you fear that he may kill you! Use your wits to escape Timothy and his family’s home by defeating each of them in battle. It’s the only way to survive!

# FEATURES: REFERENCE

# 1. Benji will escape tank and have to fight Timothy first in his bedroom. Turn based match with health deduction by attacks

# 2. Story asks you what would you like to do next, you will run into mom in the dining room

# 3. Story asks you what you would like to do, living room with front door will lead to dad as final boss

# 4. If your health depletes to 0, it's game over and are taken back to the tank. If family member is at 0, they faint or cry/scream whatever

# 5. If you die you will be asked if you want to play again. If not, exit the program

# =====================================

import time
import sys
import os
import random

##### ENEMY ATTRIBUTES ###### COMMENT
timothy = {
    "name": "Timothy",
    "health": 10,
    "attack": random.randint(0, 10)
}

mom = {
    "name":  "Mom",
    "health": 10,
    "attack": random.randint(0, 10)
}

dad = {
    "name": "Dad",
    "health": 10,
    "attack": random.randint(0, 10)
}

##### BENJI CLASS ###### COMMENT
class Benji:
    def __init__(self):
        self.name = "Benji"
        self.health = 50
        self.attack = random.randint(5, 10)
    
    def bite(self):
        decHealth = timothy["health"] - self.attack
        timothy["health"] = decHealth
        #bite will decrease using self.attack from enemy's health value in dict
        decHealthMom = mom["health"] - self.attack
        mom["health"] = decHealthMom
        
        decHealthDad = dad["health"] - self.attack
        dad["health"] = decHealthDad
    
    def run(self):
        print("You try to run, but they block your way!")
    
    def scratch(self):
        decHealth2 = timothy["health"] - self.attack
        timothy["health"] = decHealth2
        #scratch will decrease using self.attack points from Timothy's health value in dict
        decHealthMom2 = mom["health"] - self.attack
        mom["health"] = decHealthMom2

        decHealthDad2 = dad["health"] - self.attack
        dad["health"] = decHealthDad2

benji = Benji()

###### TITLE SCREEN VISUALS ###### COMMENT
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
    print('        ©2022 Amanda H.       ')


###### GAME OVER ###### COMMENT
# This shows if the prompt() loop's condition (Benji is above 0 health) is true

def gameOver():
    print("##############################")
    print("#         GAME OVER          #")
    print("##############################")
    print("\n")
    print("You were captured... ")
    print("\n")
    opts = ["yes", "no"]
    playAgain = input("Would you like to play again? yes or no: > ")
    if playAgain.lower() == "yes":
        titleScreen()
    elif playAgain.lower() == "no":
        print("Exiting game")
        sys.exit()
    while playAgain.lower() not in opts:
        print("Unknown action, try again")
        playAgain = input("> ")

# gameOver()

###### MENU LOGIC ###### COMMENT
def mainMenu():
    option = input("> ")
    if option.lower() == ("play"):
        setupGame()
    elif option.lower() == ("quit"):
        print("Exiting game")
        sys.exit()
    while option.lower() not in ['play', 'quit']: #if command isn't play or quit, repeat
        print("Please enter a valid command: ")
        option = input("> ")
        if option.lower() == ("play"):
            setupGame()
        elif option.lower() == ("quit"):
            print("Quitting")
            sys.exit()

def youEscaped():
    os.system('clear')
    print("                              ")
    print(".'.'.'.'.'.'.'.'.'.'.'.'.'.'.'.")
    print("##############################")
    print("#       YOU   ESCAPED!       #")
    print("##############################")
    print("'.'.'.'.'.'.'.'.'.'.'.'.'.'.'.'")
    print("                              ")
    end1 = "Congratulations! You are officially a free bearded dragon!\n"
    end2 = "Other bearded dragons will speak of your tales for centuries...\n"

    for char in end1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(1.5)
    print("                              ")

    for char in end2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1.5)
    
    opts = ["yes", "no"]
    print("                              ")
    playAgain = input("Would you like to play again? yes or no: > ")
    if playAgain.lower() == "yes":
        titleScreen()
        mainMenu()
    elif playAgain.lower() == "no":
        print("Thanks for playing!")
        sys.exit()
    while playAgain.lower() not in opts:
        print("Unknown action, try again")
        playAgain = input("> ")

# youEscaped()

###### END DIALOGUE ###### COMMENT

def setupEndDialogue():
    print("##############################")
    print("                              ")
    print("                              ")
    script1 = "You have made it to the end!\n"
    script2 = "The whole family is gone and you survived! \n"
    
    for char in script1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(1.5)

    for char in script2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(1.5)

    print("                              ")
    print("                              ")
    print("##############################")
    time.sleep(1.5)
    
    
    youEscaped()

# setupEndDialogue()


###### PROMPT TO FIGHT DAD ###### COMMENT

moves = ['bite', 'run', 'scratch', 'quit']

def prompt3():
    firstFight3 = False
    dad["health"] = 10
    benji.health = 50
    while not firstFight3:
        while benji.health > 0:

            dadName = dad["name"]
            dadHealth = dad["health"]
            dadAttack = dad["attack"]

            if dadHealth > 0 and firstFight3 == True:
                        print(f"It's Mom's turn. She grabs you and hurts you by {dadAttack} health!")
            elif dadHealth <= 0:
                    print("Dad flees!")
            firstFight = True

            if dadHealth <= 0:
                setupEndDialogue()
                sys.exit()
            print("                              ")
            print("                              ")
            print(f"{benji.name}'s Health: {benji.health}")
            print(f"{dadName}'s Health: {dadHealth}")
            print("\n" + "==============================")
            print("     What would you like to do?")
            print("Please type one of the four options: ")

            print("         --   bite   --")
            print("         --   run    --")
            print("         --  scratch --")
            print("         --   quit   --")
            print("==============================")
            action = input("> ")
            if action.lower() == 'bite':
                benji.bite() # decHealth = enemyDict["health"] - self.attack
                print("==============================")
                print(f"You bite Dad! He loses {benji.attack} health")

            elif action.lower() == 'run':
                benji.run() # Prints and forfeits Benji's turn
                print("==============================")

            elif action.lower() == 'scratch':
                benji.scratch() # decHealth2 = enemyDict["health"] - self.attack
                print("==============================")
                print(f"You scratch Dad! He loses {benji.attack} health")
            elif action.lower() == 'quit':
                print("Exiting game")
                sys.exit()
            while action.lower() not in moves:
                print("Unknown action, try again")
                action = input("> ")


            hurtBenji = benji.health - dadAttack
            benji.health = hurtBenji
        gameOver()
# prompt3()

###### GAME DIALOG/CONTENT PART 3 ###### COMMENT
def setupPart3():
    script1 = "You have made it to part 3!\n"
    script2 = "Here comes the final battle: \n"
    print("\n")
    print("\n")
    for char in script1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(1)

    for char in script2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1)
        
    prompt3()


# setupPart3()



###### PROMPT TO FIGHT MOM ###### COMMENT

def prompt2():
    firstFight2 = False
    mom["health"] = 10
    benji.health = 50
    while not firstFight2:
        while benji.health > 0:

            momName = mom["name"]
            momHealth = mom["health"]
            momAttack = mom["attack"]

            if momHealth > 0 and firstFight2 == True:
                        print(f"It's Mom's turn. She grabs you and hurts you by {momAttack} health!")
            elif momHealth <= 0:
                    print("Mom flees!")
            firstFight = True

            if momHealth <= 0:
                setupPart3()
                sys.exit()
            print("                              ")
            print("                              ")
            print(f"{benji.name}'s Health: {benji.health}")
            print(f"{momName}'s Health: {momHealth}")
            print("\n" + "==============================")
            print("     What would you like to do?")
            print("Please type one of the four options: ")

            print("         --   bite   --")
            print("         --   run    --")
            print("         --  scratch --")
            print("         --   quit   --")
            print("==============================")
            action = input("> ")
            if action.lower() == 'bite':
                benji.bite() # decHealth = timothy["health"] - self.attack
                print("==============================")
                print(f"You bite Mom! She loses {benji.attack} health")

            elif action.lower() == 'run':
                print("==============================")
                benji.run() # Prints and forfeits Benji's turn

            elif action.lower() == 'scratch':
                benji.scratch() # decHealth2 = timothy["health"] - self.attack
                print("==============================")
                print(f"You scratch Mom! She loses {benji.attack} health")
            elif action.lower() == 'quit':
                print("Exiting game")
                sys.exit()
            while action.lower() not in moves:
                print("Unknown action, try again")
                action = input("> ")


            hurtBenji = benji.health - momAttack
            benji.health = hurtBenji
        gameOver()

# prompt2()

###### GAME DIALOGUE/CONTENT PART 2 ###### COMMENT

def setupPart2():
    text1 = "You run past Timothy while he's busy crying and waddle down the hallway.!\n"
    text2 = "It sounds quiet...\n"
    text3 = "... Too quiet.\n"
    text4 = "You make your way to what looks like the dining room, then suddenly stop in your tracks.\n"
    text5 = "Timothy's mother, a larger and more flabby version of a human, is standing there, staring at you.\n"
    text6 = "You freeze. You aren't sure what to do.\n "
    text7 = "She immediately stampedes towards you like a bull with a look of aggravation!\n"
    text8 = "Time to fight...!\n"
    print("\n")
    print("\n")
    for char in text1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(1)

    for char in text2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1)
    
    for char in text3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1)

    for char in text4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1)

    for char in text5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1)

    for char in text6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1)

    for char in text7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1)

    for char in text8:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1)
    
    prompt2()
# setupPart2()

###### PROMPT TO FIGHT TIMOTHY ###### COMMENT

def prompt():
    firstFight = False
    while not firstFight:
        while benji.health > 0:
            timName = timothy["name"]
            timHealth = timothy["health"]
            timAttack = timothy["attack"]
            
            if timHealth > 0 and firstFight == True:
                    print(f"It's Timothy's turn. He grabs you and hurts you by {timAttack} health!")
            elif timHealth <= 0:
                print("Timothy flees!")
            firstFight = True
            
            if timHealth <= 0:
                setupPart2()
                sys.exit()
            print("\n")
            print(f"{benji.name}'s Health: {benji.health}")
            print(f"{timName}'s Health: {timHealth}")
            print("\n" + "==============================")
            print("     What would you like to do?")
            print("Please type one of the four options: ")

            print("         --   bite   --")
            print("         --   run    --")
            print("         --  scratch --")
            print("         --   quit   --")
            print("==============================")
            action = input("> ")
            if action.lower() == 'bite':
                benji.bite()
                print("==============================")
                print(f"You bite Timothy! He loses {benji.attack} health")
            elif action.lower() == 'run':
                benji.run()
                print("==============================")
            elif action.lower() == 'scratch':
                benji.scratch()
                print("==============================")
                print(f"You scratch Timothy! He loses {benji.attack} health")
            elif action.lower() == 'quit':
                print("Exiting game")
                sys.exit()
            while action.lower() not in moves:
                print("Unknown action, try again")
                action = input("> ")

            hurtBenji = benji.health - timAttack
            benji.health = hurtBenji
        gameOver()

# prompt()

###### GAME DIALOG/CONTENT PART 1 ###### COMMENT

def setupGame():
    os.system('clear')

    speech1 = "You are Benji, a young but determined bearded dragon that was just adopted by a loving family.\n"
    speech2 = "You came home in a small kennel only to find out that the family’s 6 year old child named Timothy is your new owner.\n"
    speech3 = "You have a strange feeling that Timothy doesn’t know how to take care of you and you fear that he may kill you!\n"
    speech4 = "Use your wits to escape Timothy and his family’s home by defeating each of them in battle. It's the only way to survive!\n"
    speech5 = "Watch out for Timothy...\n"
    speech6 = "... And his family. \n"
    print("                              ")

    time.sleep(1.5)
    
    for char in speech1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1.5)
    print("                              ")

    for char in speech2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1.5)
    print("                              ")

    for char in speech3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(1.5)
    print("                              ")

    for char in speech4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1.5)
    print("                              ")

    for char in speech5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    
    time.sleep(1.5)
    print("                              ")

    for char in speech6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    
    time.sleep(1.5)
    print("                              ")

    dialog1 = "You are in Timothy's room inside of a glass tank.\n"
    dialog2 = "After a few hours of basking under your heat lamp and laying around, you know very well that Timothy didn't remember to feed you any bugs today. This kid is going to starve you to death!\n"
    dialog3 = "You've finally decided. You are officially going to escape. For good. \n"
    dialog4 = "You run towards the glass and start glass surfing, repeatedly tapping your snout against it.\n"
    dialog5 = "Timothy gets aggravated and opens your tank doors out of frustration. This is your chance!\n"
    dialog6 = "You run through the doors and scramble your way to the bedroom entrance, when Timothy steps over you and blocks you from leaving his room!\n"
    
    dialog7 = "Time to fight...!\n"
    print("##############################")
    print("                              ")
    
    for char in dialog1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1.5)
    print("                              ")

    for char in dialog2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1.5)
    print("                              ")

    for char in dialog3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1.5)
    print("                              ")

    for char in dialog4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1.5)
    print("                              ")

    for char in dialog5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1.5)
    print("                              ")

    for char in dialog6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(1.5)
    print("                              ")

    for char in dialog7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    
    time.sleep(1.5)
    print("                              ")

    




titleScreen()
mainMenu() # When you click play, it goes to the setupGame()
prompt()



titleScreen() #keep this at bottom














