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


def special_select():
    global specialty, health, strength, defense
    clear_screen()
    lbl()
    print("Next, let's select a specialty.")
    lbl()
    print("1. medical knowledge. Add 5 to health")
    print("2. berserker. Add 4 to attack")
    print("3. technical. Permanently gain 4 extra defense")
    lbl()
    special_input = input("Specialty: ")
    lbl()

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

    elif special_select == "exit":
        exit()

    else:
        clear_screen()
        print("please select a specialty by typing the number of the specialty.")
        special_select()


def name_select():
    global name
    clear_screen()
    print("Alright. What is your name fair adventurer?")
    name = input("Name: ")
    game_start()  # This will be used later.


# Finally, it's time to write some actual game!
# But before we jump into that, I'm going to provide a link to a pastebin containing the code from steps 1-7 so you
# can compare as needed.
# https://pastebin.com/mwBtUvGS

# Now then, let's get into our game.

# First, let's set up our game_start function
# Feel free to just copy my code, it's all stuff you've learned before.
def game_start():
    clear_screen()
    lbl()
    print("Welcome to the arena! Here you will face enemy after enemy in deadly combat until you either run out of oponents, or die.")
    print("Would you like to start with a warmup? (tutorial)")
    lbl()
    tutorial = input("Do a warmup?(y/n): ")
    if tutorial == "y":
        print("Alright, let's get you up to speed.")
        tut() # This function will be created next.
    else:
        print("Straight into the thick of it eh? I like your style son. ")
        ####

# Once you've made your basic game_start function, we need to write our tutorial. Truth be told, this part is
# super boring and doesn't do anything new so I'll just provide a pastebin with the code. Take some time to 
# study it before we move on. 
# https://pastebin.com/4CQjvwzL


def tut():
    global enemy_current_health, enemy_health, enemy_defense, enemy_strength, enemy_name

    print("Let's get to it then. For your warmup let's have a quick sparring match.")
    time.sleep(5)
    clear_screen()
    lbl()
    print("First let's explain how this works.")
    lbl()
    print("Attack rating: This is a measure of your ability to damage others.")
    print("Defense rating: This is a measure of your ability to absorb damage.")
    print("Health: This is how much damage you can take before death.")
    lbl()
    input("Press enter to continue...")
    clear_screen()
    lbl()
    print("Attack and defense rating is randomly generated when you create your character. This number depends on your class and will be generated within a range.")
    print("Health is also generated on character creation based on class.")
    lbl()
    print("After each win you obtain, you will be given the option to upgrade 1 of your stats by 1 point.")
    print("Use your points wisely. Each victory you obtain will raise the difficulty of your enemies.")
    lbl()
    print("Alright, let's get into it kid.")
    lbl()
    input("Press enter to continue...")
    clear_screen()
    print("So first, let's basic combat. To begin with, you'll see 2 info bars. First is the enemies info. Second is yours.")
    lbl()
    print("Below the info bars, you'll find your available actions. Let's start easy.")
    lbl()
    input("Press enter to begin battle...")
    clear_screen()
    enemy_health = 20
    enemy_current_health = enemy_health
    enemy_strength = 1
    enemy_defense = 3
    enemy_name = "Sir Jacoby Brundlesworth III"
    enemy_stats()
    print("This is the standard battle UI for battle stats. Next, let's look at your battle options.")
    input("Press enter to continue...")
    clear_screen()
    lbl()
    print("What would you like to do?")
    lbl()
    print("attack")
    print("block")
    print("heal")
    lbl()
    print("As you can see, you have 3 options. Attack, Block, and Heal. ")
    print("The attack option is as simple as it sounds. Attack your opponent.")
    print("The block option is also simple. When blocking, you resist all damage but can't do anything else.")
    print("The heal option will randomly heal between 0 and 10 health. Use it wisely as it will leave you open for attack.")
    lbl()
    print("Alright that's it for the basic tutorial. Let's get into some real combat, shall we? After sparring you'll be thrown right into the arena!")
    input("Press enter to continue...")
    clear_screen()
    ####
