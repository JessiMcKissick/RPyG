import os
import random
import time

version = "0.2"
lb = "-----------------------------------------------------------------------------"
def lbl():
    print(lb)

def br():
    print(" ")

def wait_note(number):
    print("NOTE: Game will continue in " + str(number) + " seconds")
    time.sleep(number)



def header():
    print("     _____        _____    _____      _____       _____")
    print(" ___|\    \   ___|\    \  |\    \    /    /|  ___|\    \ ")
    print("|    |\    \ |    |\    \ | \    \  /    / | /    /\    \ ")
    print("|    | |    ||    | |    ||  \____\/    /  /|    |  |____|")
    print("|    |/____/ |    |/____/| \ |    /    /  / |    |    ____")
    print("|    |\    \ |    ||    ||  \|___/    /  /  |    |   |    |")
    print("|    | |    ||    ||____|/      /    /  /   |    |   |_,  |")
    print("|____| |____||____|            /____/  /    |\ ___\___/  /|")
    print("|    | |    ||    |           |`    | /     | |   /____ / |")
    print("|____| |____||____|           |_____|/       \|___|    | /")
    print("  \(     )/    \(                )/            \( |____|/ ")

def clear_screen():
    # Todo: Write a more robust system that detects the OS and uses the relevant command.
    os.system("cls")

def intro():
    clear_screen()
    header()
    print("Welcome to RPyG version " + version + "!")
    print(lb)
    print("In this text based game, your goal is to survive as many consecutive battles in a row as possible.")
    print("In the next step, you will create your character by selecting your class, a specialty, and name your character.")
    print(lb)
    print("Keep in mind: This game is meant to be played in single sittings and as such you cannot save.")
    lbl()
    input("Press enter to continue...")
    print("NOTE")
    app_main()

def app_main():
    clear_screen()
    header()
    print(lb)
    print("First, let's pick a class.")
    print("warrior. Balance between attack rating and defense rating. Good health.")
    print("wizard. A strong magical class with insane power but terrible defenses.")
    print("falanx. A heavily armored defender class with massive defense but mediocre offense.")
    class_input = input("Class choice: ")
    print(lb)
    if class_input == "warrior" or class_input == "wizard" or class_input == "falanx":
        print("Welcome, mighty " + class_input + "!")
        class_stats(class_input)
    elif class_input == "exit":
        exit()
        clear_screen()
    elif class_input == "dm":
        print("Dev skip started.")
        input("Press enter to begin.")
        global health, defense, strength
        strength = 15
        defense = 15
        health = 15
        current_health = health
        special_select()
    else:
        print("Please type one of the following: warrior, wizard, falanx.")
        app_main()
    


strength = 0
defense = 0
health = 0
current_health = 0
specialty = 0
name = "null"

victory_count = 0

enemy_strength = 0
enemy_defense = 0
enemy_health = 0
enemy_current_health = 0
enemy_name = "null"

def class_stats(class_choice):
    global current_health, health, strength, defense
    header()
    print("Note: stats are randomly generated based on your class choice.")
    print(lb)
    if class_choice == "warrior":
        strength = random.randint(2,5)
        defense = random.randint(2,5)
        health = random.randint(20,30)
        current_health = health
        print("You, fine warrior have: " + str(strength) + " attack. " + str(defense) + " defense. " + str(health) + " health.")
    elif class_choice == "wizard":
        strength = random.randint(5,15)
        defense = random.randint(0,3)
        health = random.randint(5,20)
        current_health = health
        print("You, fine warrior have: " + str(strength) + " attack. " + str(defense) + " defense. " + str(health) + " health.")
    elif class_choice == "falanx":
        strength = random.randint(1,5)
        defense = random.randint(5,15)
        health = random.randint(1,40)
        current_health = health    
        print("You, fine warrior have: " + str(strength) + " attack. " + str(defense) + " defense. " + str(health) + " health.")
    special_select()

def special_select():
    global specialty, health, strength, defense
    clear_screen()
    header()
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
        name_select()

    elif special_input == "2":
        specialty = 2
        strength += 4
        name_select()

    elif special_input == "3":
        specialty = 3
        defense += 4
        name_select()
    elif special_select == "exit":
        exit()
    else:
        clear_screen()
        print("please select a specialty by typing the number of the specialty.")
        special_select()

def name_select():
    global name, strength, defense, health
    clear_screen()
    header()
    print("Alright. What is your name fair adventurer?")
    name = input("Name: ")
    if name == "RPyG" or name == "rpyg":
    # Damn I miss cheatcodes ;)
        strength += 100
        defense += 100
        health += 500
    elif name == "The Legend":
        strength += 9999
    elif name == "Tiny Tim":
        strength = 0
        defense = 0
        health = 1
    elif name == "Kieran M":
        print("You cheeky bugger.")
        exit()
    elif name == "InFiNiTy":
        print("Overkill enabled.")
        strength = 9999999
        defense = 9999999
        health = 999999999


    game_start()

def game_start():
    clear_screen()
    lbl()
    print("Welcome to the arena! Here you will face enemy after enemy in deadly combat until you either run out of oponents, or die.")
    print("Would you like to start with a warmup? (tutorial)")
    lbl()
    tutorial = input("Do a warmup?(y/n): ")
    if tutorial == "y":
        print("Alright, let's get you up to speed.")
        tut()
    else:
        print("Straight into the thick of it eh? I like your style son. ")
        battle_init()


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
    print("The attack option is as simple as it sounds. Attack your oponent.")
    print("The block option is also simple. When blocking, you resist all damage but can't do anything else.")
    print("The heal option will randomly heal between 0 and 10 health. Use it wisely as it will leave you open for attack.")
    lbl()
    print("Alright that's it for the basic tutorial. Let's get into some real combat, shall we? After sparring you'll be thrown right into the arena!")
    input("Press enter to continue...")
    clear_screen()
    battle_handler()


def enemy_stats():
    lbl()
    print(enemy_name)
    print("Attack: " + str(enemy_strength) + " | Defense: " + str(enemy_defense) + " | Health: " + str(enemy_current_health))
    lbl()
    print(name)
    print("Attack: " + str(strength) + " | Defense: " + str(defense) + " | Health: " + str(current_health))
    lbl()

def battle_options():
    lbl()
    print("What would you like to do?")
    lbl()
    print("1. attack")
    print("2. block")
    print("3. heal")
    lbl()
    choice = input("Choice: ")
    if choice == "attack" or choice == "1":
        return 1
    elif choice == "block" or choice == "2":
        return 2
    elif choice == "heal" or choice == "3":
        return 3
    elif choice == "exit":
        clear_screen()
        exit()


def battle_init():
    clear_screen()
    global name, enemy_name, enemy_health, enemy_current_health, enemy_strength, enemy_defense, strength, defense, health, current_health    
    if victory_count > 0:
        print("Congrats on your victory! It's time to select a stat to permanently increase...")
        lbl()
        print("1. Attack. Permanently raise attack by 1 point.")
        print("2. Defense. Permanently raise defense by 1 point.")
        print("3. Health. Permanently raise health by 2 points.")
        lbl()
        upgrade_choice = input("What is your choice: ")
        if upgrade_choice == "1" or upgrade_choice == "attack":
            strength += 1
            print("Your attack is now " + str(strength))
            input("Press enter to continue...")
        elif upgrade_choice == "2" or upgrade_choice == "defense":
            defense += 1
            print ("Your defense is now " + str(defense))
            input("Press enter to continue...")
        elif upgrade_choice == "3" or upgrade_choice == "health":
            health += 2
            print ("Your standard health is now " + str(health))
            input("Press enter to continue...")
        elif upgrade_choice == exit:
            exit()
        else:
            print("I didn't understand that input... Try again.")
            input("Press enter to continue...")
            clear_screen()
            battle_init()

    if victory_count%10 == 0 and victory_count != 0:
        name_int = random.randint(0,(len(enemy_name_options) - 1))
        name_int_2 = random.randint(0,(len(enemy_surname) - 1))
        enemy_name = enemy_name_options[name_int] + " " + enemy_surname[name_int_2]
        enemy_health = (random.randint(5,15) + (victory_count * 3))
        enemy_current_health = enemy_health
        enemy_strength = (random.randint(2,10) + (victory_count + 5))
        enemy_defense = (random.randint(0,10) + (victory_count * 2))
        current_health = health
        clear_screen()
        print("Your victory count is now: " + str(victory_count))
        lbl()
        print("And now for our next allstar match: " + name + " VS. " + enemy_name + " !")
        lbl()
        input("Press enter to begin battle...")
        clear_screen()
        battle_handler()
        
    else:
        name_int = random.randint(0,(len(enemy_name_options) - 1))
        name_int_2 = random.randint(0,(len(enemy_surname) - 1))
        enemy_name = enemy_name_options[name_int] + " " + enemy_surname[name_int_2]
        enemy_health = (random.randint(5,15) + victory_count)
        enemy_current_health = enemy_health
        enemy_strength = (random.randint(2,10) + victory_count)
        enemy_defense = (random.randint(0,10) + victory_count)
        current_health = health

        clear_screen()
        print("Your victory count is now: " + str(victory_count))
        lbl()
        print("And for our next match: " + name + " VS. " + enemy_name + " !")
        lbl()
        input("Press enter to begin battle...")
        clear_screen()
        battle_handler()

def battle_handler():
    global health, current_health, enemy_health, enemy_current_health, strength, enemy_strength, defense, enemy_defense, victory_count
    enemy_stats()
    br()
    br()
    br()
    br()
    br()
    br()
    br()
    br()
    choice = battle_options()
    enemy_action = random.randint(1,3)
    print(str(choice))
    clear_screen()
    
    random_attack_modifier_enemy = random.randint(round(enemy_strength / 2), round(enemy_strength * 2))
    if choice == 1:
        random_attack_modifier = random.randint(round(strength / 2), round(strength * 2))
        if enemy_action != 2 and (random_attack_modifier - enemy_defense) > 0:
            print(name + " attacks " + enemy_name + " for " + str(random_attack_modifier) + "-" + str(enemy_defense) + " damage. (" + str(random_attack_modifier - enemy_defense) + ")")
            enemy_current_health = (enemy_current_health - (random_attack_modifier - enemy_defense))
            if enemy_current_health < 1:
                clear_screen()
                lbl()
                print("Enemy: " + enemy_name + " dies. R.I.P.")
                print("Congratulations on your victory!")
                input("Press enter to continue...")
                victory_count += 1
                lbl()
                battle_init()
            
        elif (strength - enemy_defense) < 0:
            print(name + " attacks " + enemy_name + " but does no damage!")
        else:
            print(name + " attacks " + enemy_name + "but is blocked!")
    
    
    elif choice == 2:
        print("You raise your defenses.")
        if enemy_action == 1:
            print(enemy_name + " attacks but is blocked!")
        elif enemy_action == 2:
            print(enemy_name + " raises their defenses.")
    
    
    elif choice == 3:
        heal_amount = random.randint(0,10)
        print(name + " heals for " + str(heal_amount) + " health.")
        current_health += heal_amount
    else:
        print("Please select a correct option.")
        battle_handler()
        
    
    if enemy_action == 3:
        heal_amount = random.randint(0,10)
        print(enemy_name + " heals for " + str(heal_amount) + " health.")
        enemy_current_health += heal_amount
    elif enemy_action == 1 and choice != 2 and (random_attack_modifier_enemy - defense) > 0:
        print(enemy_name + " attacks for " + str(random_attack_modifier_enemy) + " -" + str(defense) + "damage! (" + str(random_attack_modifier_enemy - defense) + ")")
        current_health = (current_health - (random_attack_modifier_enemy - defense))
        if current_health < 1:
            clear_screen()
            print(enemy_name + " kills " + name + ". R.I.P.")
            print("Game over.")
            time.sleep(5)
            game_over()
    elif (strength - enemy_defense) < 0:
        print(name + " attacks " + enemy_name + " but does no damage!")
    else:
        print(enemy_name + " attacks but is blocked!")
    battle_handler()



def game_over():
    clear_screen()
    new_game = input("Start a new game? y/n: ")
    if new_game == "y":
        clear_screen()
        intro()
    elif new_game == "n":
        exit()
    else:
        game_over()



enemy_name_options = ["Bob", "Tim", "George", "Bigg", "Lil'", "The great", "Spid", "Kay", "Aaron", "Phillip", "Korrin", "David", "Kieran", "Cassandra", "Daniel", "Jesus", "Adam", "Jessica", "The great big", "Sir Benedict"]
enemy_surname = ["Kurpshank", "Smellwich", "Landar", "Dick", "Spork", "Kumkwat", "Beardsly", "The angry", "The depressed", "The violent", "McLeary", "Goth", "Jenkins", "Monarch of RPyG", "Jowels"]

intro()

