import os  # Allows you to utilize OS functions.
import random  # Allows you to utilize math randomization and the likes.
import time  # Allows access to time. This will mostly be used for delays.
import platform  # We'll use this to find the current devices platform.

version = "0.0"
lb = "-----------------------------------------------------------------------------"


def lbl():
    print(lb)


def br():
    print(" ")


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def intro():
    clear_screen()
    print("Welcome to RPyG version " + version + "!")
    lbl()
    print("In this text based game, your goal is to survive as many consecutive battles in a row as possible.")
    print("In the next step, you will create your character by selecting your class, a specialty, and name your character.")
    lbl()
    print("Keep in mind: This game is meant to be played in single sittings and as such you cannot save.")
    lbl()
    input("Press enter to continue...")
    print("NOTE")


def app_start():
    clear_screen()
    lbl()
    print("First, let's pick a class.")
    print("1. warrior. Balance between attack rating and defense rating. Good health.")
    print("2. wizard. A strong magical class with insane power but terrible defenses.")
    print("3. falanx. A heavily armored defender class with massive defense but mediocre offense.")
    class_input = input("Class choice: ")
    lbl()
    if class_input == "warrior" or class_input == "wizard" or class_input == "falanx" or class_input == "1" or class_input == "2" or class_input == "3":
        print("Welcome, mighty " + class_input + "!")
        class_stats(class_input)
    elif class_input == "exit":
        exit()
        clear_screen()
    else:
        print("Please type one of the following: warrior, wizard, falanx.")
        app_start()


strength = 0
defense = 0
health = 0
current_health = 0
specialty = 0
name = "null"

enemy_strength = 0
enemy_defense = 0
enemy_health = 0
enemy_current_health = 0
enemy_name = "null"

victory_count = 0


def class_stats(class_choice):
    global current_health, health, strength, defense
    print("Note: stats are randomly generated based on your class choice.")
    print(lb)
    if class_choice == "warrior" or class_choice == "1":
        strength = random.randint(2, 5)
        defense = random.randint(2, 5)
        health = random.randint(20, 30)
        current_health = health
        print("You, fine warrior have: " + str(strength) + " attack. " +
              str(defense) + " defense. " + str(health) + " health.")
    elif class_choice == "wizard" or class_choice == "2":
        strength = random.randint(5, 15)
        defense = random.randint(0, 3)
        health = random.randint(5, 20)
        current_health = health
        print("You, fine warrior have: " + str(strength) + " attack. " +
              str(defense) + " defense. " + str(health) + " health.")
    elif class_choice == "falanx" or class_choice == "3":
        strength = random.randint(1, 5)
        defense = random.randint(5, 15)
        health = random.randint(1, 40)
        current_health = health
        print("You, fine warrior have: " + str(strength) + " attack. " +
              str(defense) + " defense. " + str(health) + " health.")
    special_select()
    # Simply add special_select to the end of your function.

# Now that we've written a system to generate our player stats based on their class selection, we need to write
# functionality that allows our players to select their special skill.

# To begin, let's write a function named special_select
def special_select():
    # Now let's make sure our relevant variables are in the global scope again.
    global specialty, health, strength, defense
    # Then draw some UI.
    clear_screen()
    lbl()
    print("Next, let's select a specialty.")
    lbl()
    # And print a list of specialties you want the player to choose from.
    print("1. medical knowledge. Add 5 to health")
    print("2. berserker. Add 4 to attack")
    print("3. technical. Permanently gain 4 extra defense")
    lbl()
    # And finally, the prompt asking for their specialty choice.
    special_input = input("Specialty: ")
    lbl()
    # Now we need to write our logic.

    # Simply write if statements, set the specialty, tweak any stats you want to for each specialty.
    if special_input == "1":
        specialty = 1
        health += 5
        ####

    elif special_input == "2":
        specialty = 2
        strength += 4
        ####

    elif special_input == "3":
        specialty = 3
        defense += 4
        ####
        
    # Now let's add functionality that allows the player to just quit during this step by typing exit.
    elif special_select == "exit":
        exit()
    # And lastly, we need some generic catchall functionality that will catch any unexpected input and output info.
    else:
        clear_screen()
        print("please select a specialty by typing the number of the specialty.")
        special_select()

# To finish up this step, we need to add the specialty selection step to our class_stats function.
# We're getting there! So far you've written over 100 lines of Python!