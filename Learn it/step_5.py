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
        # Let's just put our class_stats function here and pass the user input class_input to it.
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

# Next, let's create the functionality to generate our players stats. 
# Each game a player starts will have different stats depending on their class, so let's write a reasonably
# robust solution. 
# NOTE: I know there are better ways to do this, but for beginners this is a good option.

# The function below will take in a string, then execute code based on the input.
def class_stats(class_choice): 
    # First, let's define our relevant variables in the global scope. This is important as our changes wont take
    # otherwise.
    global current_health, health, strength, defense
    print("Note: stats are randomly generated based on your class choice.")
    print(lb)
    # Now we get to the meat. First we write an if statement for our first option: Warrior.
    if class_choice == "warrior" or class_choice == "1":
        # Then let's set our 3 core stats to a random integer. For warrior, let's give them very basic stats.
        strength = random.randint(2, 5) 
        # This will generate a random number from 2 to 5 using the random.randint() function. 
        # The first number in randint is the low end, and the second is the high end.
        defense = random.randint(2, 5)
        # Next let's give them decent defense and a reasonably high health.
        health = random.randint(20, 30)
        # Lastly, let's set the players current health to be equal to health.
        current_health = health
        # And for good measure, let's let the player know their stats.
        print("You, fine warrior have: " + str(strength) + " attack. " +
              str(defense) + " defense. " + str(health) + " health.")
    # Now let's just repeat this for the other 2 classes.
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
    ####

#To finish up this step, let's go back up to our start function and add our class generation function.
