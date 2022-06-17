
import time
import sys
import os
import random

##### ENEMY ATTRIBUTES ######
timothy = {
    "name": "Timothy",
    "health": 30
}

mom = {
    "name":  "Mom",
    "health": 35
}

dad = {
    "name": "Dad",
    "health": 40
}

##### BENJI CLASS ###### 
class Benji:
    def __init__(self):
        self.name = "Benji"
        self.health = 50
    
    def bite(self):
        bite = "C H O M P . . . !\n"
        print("                              ")
        for char in bite:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.2)
        time.sleep(0.5)
    
    def run(self):
        runMessage = "You try to run, but they block your way!"
        print("                              ")
        for char in runMessage:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        time.sleep(0.5)
    
    def scratch(self):
        scratch = "S C R A T C H . . . !\n"
        print("                              ")
        for char in scratch:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.2)
        time.sleep(0.5)

benji = Benji()

###### TITLE SCREEN VISUALS ###### 
def titleScreen():
    os.system('clear') # Moves screen up
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


###### GAME OVER ###### 

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
        print("Thanks for playing!")
        sys.exit()
    while playAgain.lower() not in opts:
        print("Unknown action, try again")
        playAgain = input("> ")

###### MENU LOGIC ###### 
def mainMenu():
    option = input("> ")
    if option.lower() == ("play"):
        setupGame()
    elif option.lower() == ("quit"):
        print("Exiting game")
        sys.exit()
    while option.lower() not in ['play', 'quit']:
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

###### END DIALOGUE ###### 

def setupEndDialogue():
    print("##############################")
    print("                              ")
    print("                              ")
    script1 = "Dad lunges towards you, his body clumsily reaching out, weak from all of the red marks that you inflicted.\n"
    script2 = "You manage to dodge out of the way and the Dad falls onto the floor like a skyscraper crashing down before your eyes.\n"
    script3 = "You did it... You actually did it. You defeated all 3 family members!\n"
    script4 = "You run out the front door, waddling with excitement knowing that you'll be eating all of the worms that you desire!\n"
    
    for char in script1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1.5)
    print("                              ")
    for char in script2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1.5)
    print("                              ")
    for char in script3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1.5)
    print("                              ")
    for char in script4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(4)
    youEscaped()


###### PROMPT TO FIGHT DAD ###### 

moves = ['bite', 'run', 'scratch', 'quit']

def prompt3():
    dad["health"] = 40
    benji.health = 50

    while benji.health > 0:

        dadName = dad["name"]
        dadHealth = dad["health"]
        randomNum = random.randint(1, 10)

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
            benji.bite() 
            print("==============================")
            print(f"You bite Dad! He loses {randomNum} health")
            decHealth5 = dad["health"] - randomNum
            dad["health"] = decHealth5
            randomNum2 = random.randint(1, 10)

            print(f"It's Dad's turn. He grabs you and hurts you by {randomNum2} health!")
            hurtBenji = benji.health - randomNum2
            benji.health = hurtBenji

        elif action.lower() == 'run':
            benji.run()
            print("==============================")

        elif action.lower() == 'scratch':
            benji.scratch()
            print("==============================")
            print(f"You scratch Dad! He loses {randomNum} health")

            decHealth6 = dad["health"] - randomNum
            dad["health"] = decHealth6
            randomNum3 = random.randint(1, 10)

            print(f"It's Dad's turn. He grabs you and hurts you by {randomNum3} health!")
            hurtBenji = benji.health - randomNum3
            benji.health = hurtBenji

        elif action.lower() == 'quit':
            print("Exiting game")
            sys.exit()
        while action.lower() not in moves:
            print("Unknown action, try again")
            action = input("> ")

    gameOver()


###### GAME DIALOG/CONTENT PART 3 ###### 
def setupPart3():
    print("##############################")
    print("                              ")
    print("                              ")
    script1 = "Mom angrily throws a tantrum in frustration at how many red marks she has and stomps out the front door of the house.\n"
    script2 = "You see that she forgets to close the front door and the house is wide open. Now is your chance! \n"
    

    for char in script1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in script2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)

    opts = ["yes", "no"]
    print("                              ")
    playAgain = input("Run to the door? yes or no: > ")
    if playAgain.lower() == "yes":
        pass
    elif playAgain.lower() == "no":
        print("                              ")
        playAgain2 = input("Oh... Um... You sure? yes or no: > ")
        if playAgain2.lower() == "yes":
            os.system('clear')
            print("                              ")
            print("Oh... Okay. Well I guess you were wanting to be a pet anyways.")
            print("                              ")
            gameOver()
        elif playAgain2.lower() == "no":
            pass
    while playAgain.lower() not in opts:
        print("Unknown action, try again")
        playAgain = input("> ")


    letsMoveOn = "Good. I'm glad! Freedom here we come.\n"

    script3 = "You waddle towards the front door as fast as your little reptilian legs can carry you.\n"
    script4 = "You feel like you're finally home free... Until you see a massive figure step in front of the doorway!\n"
    script5 = "The father, a massive and muscular giant, is blocking your ticket to freedom!\n"
    script6 = "Let's do this. This is the moment that you've been waiting for.\n"

    timeToFight = "Time to fight...!\n"
    print("                              ")
    for char in letsMoveOn:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in script3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in script4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in script5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in script6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in timeToFight:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(1)
    prompt3()

###### PROMPT TO FIGHT MOM ###### 

def prompt2():
    mom["health"] = 35
    benji.health = 50
    
    while benji.health > 0:

        momName = mom["name"]
        momHealth = mom["health"]
        randNumber = random.randint(1, 10)

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
            benji.bite()
            print("==============================")
            print(f"You bite Mom! She loses {randNumber} health")
            decHealth3 = mom["health"] - randNumber
            mom["health"] = decHealth3
            randNumber2 = random.randint(1, 10)

            print(f"It's Mom's turn. He grabs you and hurts you by {randNumber2} health!")
            hurtBenji = benji.health - randNumber2
            benji.health = hurtBenji

        elif action.lower() == 'run':
            print("==============================")
            benji.run()

        elif action.lower() == 'scratch':
            benji.scratch() 
            print("==============================")
            print(f"You scratch Mom! She loses {randNumber} health")
            
            decHealth4 = mom["health"] - randNumber
            mom["health"] = decHealth4
            randNumber3 = random.randint(1, 10)

            print(f"It's Mom's turn. She grabs you and hurts you by {randNumber3} health!")
            hurtBenji = benji.health - randNumber3
            benji.health = hurtBenji

        elif action.lower() == 'quit':
            print("Exiting game")
            sys.exit()
        while action.lower() not in moves:
            print("Unknown action, try again")
            action = input("> ")

    gameOver()

###### GAME DIALOGUE/CONTENT PART 2 ###### 

def setupPart2():
    print("##############################")
    print("                              ")
    print("                              ")
    text1 = "You run past Timothy while he's busy crying and waddle down the hallway.\n"
    text2 = "It sounds quiet...\n"
    text3 = "... Too quiet.\n"
    text4 = "You make your way to what looks like the dining room, then suddenly stop in your tracks.\n"
    text5 = "Timothy's mother, a larger and more flabby version of a human, is standing there, staring at you.\n"
    text6 = "You freeze. You aren't sure what to do.\n "
    text7 = "She immediately stampedes towards you like a bull with a look of aggravation!\n"
    text8 = "Time to fight...!\n"

    for char in text1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in text2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in text3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in text4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in text5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in text6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in text7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1)
    print("                              ")
    for char in text8:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(1)
    print("                              ")

    prompt2()

###### PROMPT TO FIGHT TIMOTHY ###### 

def prompt():

    while benji.health > 0:
        timName = timothy["name"]
        timHealth = timothy["health"]
        randNum = random.randint(1, 10)
            
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
            print(f"You bite Timothy! He loses {randNum} health")
            decHealth = timothy["health"] - randNum
            timothy["health"] = decHealth
            randNum2 = random.randint(1, 10)

            print(f"It's Timothy's turn. He grabs you and hurts you by {randNum2} health!")
            hurtBenji = benji.health - randNum2
            benji.health = hurtBenji

        elif action.lower() == 'run':
            benji.run()
            print("==============================")
        elif action.lower() == 'scratch':
            benji.scratch()
            print("==============================")
            print(f"You scratch Timothy! He loses {randNum} health")

            decHealth2 = timothy["health"] - randNum
            timothy["health"] = decHealth2
            randNum3 = random.randint(1, 10)

            print(f"It's Timothy's turn. He grabs you and hurts you by {randNum3} health!")
            hurtBenji = benji.health - randNum3
            benji.health = hurtBenji

        elif action.lower() == 'quit':
            print("Exiting game")
            sys.exit()
        while action.lower() not in moves:
            print("Unknown action, try again")
            action = input("> ")
                
    gameOver()

###### GAME DIALOG/CONTENT PART 1 ###### 

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
mainMenu()
prompt()
titleScreen()