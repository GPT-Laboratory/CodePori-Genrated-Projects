import time

# Function to add a small delay for a better reading experience
def delay_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

# Introduction to the game
def introduction():
    delay_print("Welcome to the Adventure Game!")
    delay_print("You find yourself in a mysterious forest.")
    delay_print("Your goal is to find a way out.")
    delay_print("Choose wisely, as your decisions will shape your destiny.")
    time.sleep(1)

# First decision point
def crossroads():
    delay_print("\nYou come to a crossroads.")
    delay_print("Do you want to go left or right? (left/right)")
    
    choice = input("> ").lower()
    
    if choice == 'left':
        dark_forest()
    elif choice == 'right':
        village_path()
    else:
        delay_print("Invalid choice. Please type 'left' or 'right'.")
        crossroads()

# Path to the dark forest
def dark_forest():
    delay_print("\nYou walk into the dark forest.")
    delay_print("The trees are thick, and the atmosphere is eerie.")
    delay_print("You hear a growling sound behind you. Do you run or investigate? (run/investigate)")
    
    choice = input("> ").lower()
    
    if choice == 'run':
        delay_print("You run as fast as you can!")
        delay_print("You stumble upon a hidden cave. Do you want to enter or keep running? (enter/run)")
        
        cave_choice = input("> ").lower()
        
        if cave_choice == 'enter':
            secret_cave()
        else:
            delay_print("You keep running until you're out of breath.")
            delay_print("Unfortunately, you are caught by a wild beast. Game Over!")
    elif choice == 'investigate':
        delay_print("You cautiously approach the sound.")
        delay_print("It's a friendly wolf! It offers to guide you out of the forest.")
        delay_print("Do you trust the wolf or refuse its help? (trust/refuse)")
        
        wolf_choice = input("> ").lower()
        
        if wolf_choice == 'trust':
            delay_print("The wolf guides you safely out of the forest. You win!")
        else:
            delay_print("You refuse the wolf's help and get lost in the forest. Game Over!")
    else:
        delay_print("Invalid choice. Please type 'run' or 'investigate'.")
        dark_forest()

# Path to the village
def village_path():
    delay_print("\nYou take the path toward the village.")
    delay_print("The village seems abandoned and quiet.")
    delay_print("You see a house with smoke coming from the chimney. Do you knock on the door or explore the village? (knock/explore)")
    
    choice = input("> ").lower()
    
    if choice == 'knock':
        stranger_house()
    elif choice == 'explore':
        village_explore()
    else:
        delay_print("Invalid choice. Please type 'knock' or 'explore'.")
        village_path()

# The player's choice to enter the cave in the dark forest
def secret_cave():
    delay_print("\nYou enter the secret cave.")
    delay_print("Inside, you find a treasure chest!")
    delay_print("Do you want to open the chest or leave it alone? (open/leave)")
    
    choice = input("> ").lower()
    
    if choice == 'open':
        delay_print("You open the chest and find gold and jewels. You win!")
    else:
        delay_print("You decide to leave the treasure alone and exit the cave.")
        delay_print("On your way out, you trip and fall. Game Over!")
    
# The player's choice to explore the village
def village_explore():
    delay_print("\nYou wander through the empty village.")
    delay_print("Suddenly, you hear a noise behind you.")
    delay_print("Do you want to hide or confront the noise? (hide/confront)")
    
    choice = input("> ").lower()
    
    if choice == 'hide':
        delay_print("You hide behind a building.")
        delay_print("A group of thieves pass by, but you remain safe. You survive and find your way out. You win!")
    elif choice == 'confront':
        delay_print("You bravely confront the noise.")
        delay_print("Unfortunately, it's a group of thieves, and they capture you. Game Over!")
    else:
        delay_print("Invalid choice. Please type 'hide' or 'confront'.")
        village_explore()

# The player's choice to knock on the door of the house with smoke
def stranger_house():
    delay_print("\nYou knock on the door.")
    delay_print("An old woman answers and invites you in.")
    delay_print("She offers you some tea. Do you accept or decline? (accept/decline)")
    
    choice = input("> ").lower()
    
    if choice == 'accept':
        delay_print("You accept the tea and feel relaxed.")
        delay_print("The woman offers you advice on how to escape the forest. You thank her and leave. You win!")
    elif choice == 'decline':
        delay_print("You politely decline and leave the house.")
        delay_print("However, as you walk away, you feel dizzy and faint. Game Over!")
    else:
        delay_print("Invalid choice. Please type 'accept' or 'decline'.")
        stranger_house()

# Function to start the game
def start_game():
    introduction()
    crossroads()

# Start the adventure
start_game()
