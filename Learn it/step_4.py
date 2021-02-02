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
        #########
    elif class_input == "exit":
        exit()
        clear_screen()
    else:
        print("Please type one of the following: warrior, wizard, falanx.")
        app_start()

# Now let's define some important variables real quick.

# Firstly let's define the players Strength, which will be used to calculate attacks,
# Defense, which will subtract damage from enemy attacks,
# Health, which will declare how much damage our player can take, 
# Current_health, which will tell the system how much health the player currently has,
# specialty, which will declare which special skill our player has,
# and Name, which we'll start as "null". This will be changed later.
strength = 0
defense = 0
health = 0
current_health = 0
specialty = 0
name = "null"

# Next, let's do the same but for our randomly generated enemies. Just leave out specialty.
enemy_strength = 0
enemy_defense = 0
enemy_health = 0
enemy_current_health = 0
enemy_name = "null"

#And lastly, let's write a basic variable integer that will be used to increase the difficulty as the game continues.
victory_count = 0

