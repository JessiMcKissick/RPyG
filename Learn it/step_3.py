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

#Now we need to start actually doing things. 
#First, we need to define the function that handles the opening of the game proper.

def app_start():
    #To start, let's draw some UI and let our user pick their class.
    clear_screen()
    lbl()
    print("First, let's pick a class.")
    print("1. warrior. Balance between attack rating and defense rating. Good health.")
    print("2. wizard. A strong magical class with insane power but terrible defenses.")
    print("3. falanx. A heavily armored defender class with massive defense but mediocre offense.")
    #You can of course make as many or as few classes as you'd like.
    #Next, let's get our users input: Their class choice.
    class_input = input("Class choice: ")
    # The above input will change the value of class_input to whatever string the user types in. 
    # The text inside of the input is just the prompt that is displayed to the user.
    lbl()
    # Now let's write our input handling logic. My example is relatively robust, albeit inefficient. 
    # Disregard the excess of pound signs, they're just placeholders.
    if class_input == "warrior" or class_input == "wizard" or class_input == "falanx" or class_input == "1" or class_input == "2" or class_input == "3":
        print("Welcome, mighty " + class_input + "!")
        #########
    elif class_input == "exit":
        exit()
        clear_screen()
    else:
        print("Please type one of the following: warrior, wizard, falanx.")
        app_start()
