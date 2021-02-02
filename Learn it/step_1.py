#First, we'll want to import some of pythons core libraries.
import os #Allows you to utilize OS functions.
import random #Allows you to utilize math randomization and the likes.
import time #Allows access to time. This will mostly be used for delays.
import platform #We'll use this to find the current devices platform.

# To get rolling, we want to create some core variables and functions we'll use throughout.
version = "0.0" #This is our version number. It serves no real use but lets the user know our version. 
lb = "-----------------------------------------------------------------------------"
# ^ This will be used to print a simple line of dashes for a hyper-basic UI.

def lbl(): #This will be used to print our line of dashes on to the terminal.
    print(lb)


def br(): # This is just a simple line break that will allow us to seperate elements
    print(" ")


def clear_screen(): # THis function will simply check our OS, and utilize the clear function to clear our screen.
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


