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

# Next up, we need to get our opener made. This will introduce your game and pass us to the main part of the game
# afterwards.


def intro(): #This function gives us a clean sleight, prints our game name and version, and provides basic info.
    # Let's go over the 3 main functionalities here.
    clear_screen() # This is our clear function we wrote earlier.
    print("Welcome to RPyG version " + version + "!") #Print is a standard function in Python to print to console
    lbl() # This is our line function we wrote in step 1.
    print("In this text based game, your goal is to survive as many consecutive battles in a row as possible.")
    print("In the next step, you will create your character by selecting your class, a specialty, and name your character.")
    lbl()
    print("Keep in mind: This game is meant to be played in single sittings and as such you cannot save.")
    lbl()
    input("Press enter to continue...") # This is an input. These normally take actual input but in this case
                                        # It's just being used to pause the function so the user can read everything.
    print("NOTE")


