import sys
import time


# dialog = [
#     input("You are a young bearded dragon..."),
#     input("You escaped the tank. Yourjourney out of this dungeon of a home starts here.")
# ]

# for item in range(len(dialog)):
#     for i in dialog[item]:
#         # print(i, end="")
#         sys.stdout.write(dialog[item][i])
#         sys.stdout.flush()
#         time.sleep(0.2)

    # print(dialog[item])


sentence = "Hello there.\n"
sentence2 = "How are you?\n"


for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)

time.sleep(1)

for char in sentence2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)






# dialog = {
#     "speech1": "You are a young bearded dragon...",
#     "speech2": "You escaped the tank. Yourjourney out of this dungeon of a home starts here."
# }

# for text in dialog:
#     for char in dialog[text]:
#         sys.stdout.write(dialog[text])
#         sys.stdout.flush()
#         time.sleep(0.05)
# print(dialog[text])



# speech1 = "You are a young bearded dragon... \n"
# speech2 = "You escaped the tank. Yourjourney out of this dungeon of a home starts here.\n"
# speech3 = "Watch out for Timothy...\n"
# speech4 = "... And his family. \n"
    
# for char in speech1:
#     sys.stdout.write(char)
#     sys.stdout.flush()
#     time.sleep(0.05)
# for char in speech2:
#     sys.stdout.write(char)
#     sys.stdout.flush()
#     time.sleep(0.05)
# for char in speech3:
#     sys.stdout.write(char)
#     sys.stdout.flush()
#     time.sleep(0.1)
# for char in speech4:
#     sys.stdout.write(char)
#     sys.stdout.flush()
#     time.sleep(0.1)