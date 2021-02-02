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
    app_start()


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
    global name
    clear_screen()
    print("Alright. What is your name fair adventurer?")
    name = input("Name: ")
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
        tut()  # This function will be created next.
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
    print("The attack option is as simple as it sounds. Attack your opponent.")
    print("The block option is also simple. When blocking, you resist all damage but can't do anything else.")
    print("The heal option will randomly heal between 0 and 10 health. Use it wisely as it will leave you open for attack.")
    lbl()
    print("Alright that's it for the basic tutorial. Let's get into some real combat, shall we? After sparring you'll be thrown right into the arena!")
    input("Press enter to continue...")
    clear_screen()
    battle_init()

# Now for the rest of the damn owl.
# At this point, this has been a long lesson and you've learned a lot, SO we're gonna rapid fire this one a little.
# (Don't worry, I'll be covering everything piece by piece.)

#First, we need to define our enemy display function that will be called each time a new battle begins.


def enemy_stats():
    lbl()
    print(enemy_name)
    # Below you can see another of Pythons core functions str(). This will take the variable inside and
    # convert it to a string.
    print("Attack: " + str(enemy_strength) + " | Defense: " +
          str(enemy_defense) + " | Health: " + str(enemy_current_health))
    lbl()
    print(name)
    print("Attack: " + str(strength) + " | Defense: " +
          str(defense) + " | Health: " + str(current_health))
    lbl()

# Next, let's set up the function that will handle our combat inputs called battle_options()


def battle_options():
    lbl()
    print("What would you like to do?")
    lbl()
    print("1. attack")
    print("2. block")
    print("3. heal")
    lbl()
    # Then get the players input and return either 1, 2 or 3. We'll use this later.
    choice = input("Choice: ")
    if choice == "attack" or choice == "1":
        return 1
    elif choice == "block" or choice == "2":
        return 2
    elif choice == "heal" or choice == "3":
        return 3
    #Don't forget the exit function!
    elif choice == "exit":
        clear_screen()
        exit()

# And now lets start making our combat functionality.
# First, let's define our battle_init() function.


def battle_init():
    clear_screen()
    # Define our globals
    global name, enemy_name, enemy_health, enemy_current_health, enemy_strength, enemy_defense, strength, defense, health, current_health
    # And write our logic.
    # First let's write the functionality that will allow you to upgrade your character after each battle.
    # First, we need to make sure this will only pop up after you've won at least 1 battle.
    if victory_count > 0:
        # Then add our informative text and UI.
        print("Congrats on your victory! It's time to select a stat to permanently increase...")
        lbl()
        print("1. Attack. Permanently raise attack by 1 point.")
        print("2. Defense. Permanently raise defense by 1 point.")
        print("3. Health. Permanently raise health by 2 points.")
        lbl()
        upgrade_choice = input("What is your choice: ")
        # Then a prompt, and the logic to handle the players choice.
        if upgrade_choice == "1" or upgrade_choice == "attack":
            strength += 1
            print("Your attack is now " + str(strength))
            input("Press enter to continue...")
        elif upgrade_choice == "2" or upgrade_choice == "defense":
            defense += 1
            print("Your defense is now " + str(defense))
            input("Press enter to continue...")
        elif upgrade_choice == "3" or upgrade_choice == "health":
            health += 2
            print("Your standard health is now " + str(health))
            input("Press enter to continue...")
        elif upgrade_choice == exit:
            exit()
        else:
            print("I didn't understand that input... Try again.")
            input("Press enter to continue...")
            clear_screen()
            battle_init()
    # Next, let's add a separate logic tree that will handle the enemy generation and pass us to the battle handler.
    # To do so, let's check if victory_count modulus 10 is equal to 0, AND the victory count is greater than 0
    if victory_count % 10 == 0 and victory_count != 0:
        # Now before we continue, we need to jump down to the bottom of our app and write a list of names that our
        # enemies can have. I'll leave a pastebin with my name sets. https://pastebin.com/E1gL9Zqn
        name_int = random.randint(0, (len(enemy_name_options) - 1))
        # The len() function returns the number of items in a list. The above line can be thought of as
        # A random number between 0 and the number of items in our list minus one. Remember that
        # Arrays start at 0 so the -1 makes sure it never picks a number above the lists items.
        name_int_2 = random.randint(0, (len(enemy_surname) - 1))
        # Then let's have the system set our enemy name as the name_int-th item in enemy_name_options
        # and the name_int_2-th item in enemy_surname.
        enemy_name = enemy_name_options[name_int] + \
            " " + enemy_surname[name_int_2]
        # Then we need to randomly generate the enemies health and set their current to their default.
        enemy_health = (random.randint(5, 15) + (victory_count * 3))
        enemy_current_health = enemy_health
        # And randomly gen their combat stats.
        enemy_strength = (random.randint(2, 10) + (victory_count + 5))
        enemy_defense = (random.randint(0, 10) + (victory_count * 2))
        # And reset the players health to their normal full amount.
        current_health = health
        clear_screen()
        # Then tell the player their count, and call out the match like below.
        print("Your victory count is now: " + str(victory_count))
        lbl()
        print("And now for our next allstar match: " +
              name + " VS. " + enemy_name + " !")
        lbl()
        input("Press enter to begin battle...")
        clear_screen()
        battle_handler()

    # Now let's write a similar function for other situations.
    else:
        name_int = random.randint(0, (len(enemy_name_options) - 1))
        name_int_2 = random.randint(0, (len(enemy_surname) - 1))
        enemy_name = enemy_name_options[name_int] + \
            " " + enemy_surname[name_int_2]
        enemy_health = (random.randint(5, 15) + victory_count)
        enemy_current_health = enemy_health
        enemy_strength = (random.randint(2, 10) + victory_count)
        enemy_defense = (random.randint(0, 10) + victory_count)
        current_health = health

        clear_screen()
        print("Your victory count is now: " + str(victory_count))
        lbl()
        print("And for our next match: " + name + " VS. " + enemy_name + " !")
        lbl()
        input("Press enter to begin battle...")
        clear_screen()
        battle_handler()

# And now, let's write the actual combat loop handler functionality.
# Create a function called battle_handler()


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
    # Now we need to summon up the battle_options menu and put any returned data into a variable called choice.
    choice = battle_options()
    # And next, our "A I". Really it's just a random number from 1-3. The enemies action will be picked by this.
    enemy_action = random.randint(1, 3)
    print(str(choice))
    clear_screen()

    # The below functionality will create a random number between the enemies strength divided by 2
    # rounded to the nearest whole number, and enemy strength * 2, rounded to the nearest whole number.
    random_attack_modifier_enemy = random.randint(
        round(enemy_strength / 2), round(enemy_strength * 2))
    # And now that we've preemptively found how much damage our enemy will do, we need to process which choice
    # our player has made, and do any work that's relevant to said choice.
    if choice == 1:
        # Similar to the enemy damage calculator, we just take the strength vars for our player and divide, multiply,
        # and round.
        random_attack_modifier = random.randint(
            round(strength / 2), round(strength * 2))
        # Now we need to find out if the enemy is going to try to block your attack.
        # All we need to do is make sure the enemy isn't blocking, and that our damage will be greater than their
        # defense.
        if enemy_action != 2 and (random_attack_modifier - enemy_defense) > 0:
            print(name + " attacks " + enemy_name + " for " + str(random_attack_modifier) + "-" +
                  str(enemy_defense) + " damage. (" + str(random_attack_modifier - enemy_defense) + ")")
            enemy_current_health = (
                enemy_current_health - (random_attack_modifier - enemy_defense))
            # And our functionality for if the enemy dies.
            if enemy_current_health < 1:
                clear_screen()
                lbl()
                print("Enemy: " + enemy_name + " dies. R.I.P.")
                print("Congratulations on your victory!")
                input("Press enter to continue...")
                victory_count += 1
                lbl()
                battle_init()
        # Then we need our functionality to tell our player when we do hit, but our damage is below the enemies
        # Defense.
        elif (strength - enemy_defense) < 0:
            print(name + " attacks " + enemy_name + " but does no damage!")
        # And finally, the functionality that goes off when the enemy is blocking.
        else:
            print(name + " attacks " + enemy_name + "but is blocked!")
    # And now our functionality for the player choosing to raise their defenses.
    elif choice == 2:
        print("You raise your defenses.")
        if enemy_action == 1:
            print(enemy_name + " attacks but is blocked!")
        #As well as a catch for when our enemy also raises their defense.
        elif enemy_action == 2:
            print(enemy_name + " raises their defenses.")

    # And of course, the player choice of healing.
    elif choice == 3:
        # Allow our player to heal by an amount, print that it happened, and change the players health.
        heal_amount = random.randint(0, 10)
        print(name + " heals for " + str(heal_amount) + " health.")
        current_health += heal_amount
    # And lastly, a catch for when the player inputs an invalid option.
    else:
        print("Please select a correct option.")
        battle_handler()

    # Now for the enemy. First let's cover the super simple functionality. The heal.
    # This is pretty much the same as our player heal but tweaked a little.
    if enemy_action == 3:
        heal_amount = random.randint(0, 10)
        print(enemy_name + " heals for " + str(heal_amount) + " health.")
        enemy_current_health += heal_amount

    # And now for our functionality for when the player isn't blocking, and the enemy is attacking.
    # We need to make sure both the above criteria are met, AND we need to make sure the enemy actually hits.
    elif enemy_action == 1 and choice != 2 and (random_attack_modifier_enemy - defense) > 0:
        print(enemy_name + " attacks for " + str(random_attack_modifier_enemy) + " -" +
              str(defense) + "damage! (" + str(random_attack_modifier_enemy - defense) + ")")
        current_health = (
            current_health - (random_attack_modifier_enemy - defense))
        # And of course the player death condition.
        if current_health < 1:
            clear_screen()
            print(enemy_name + " kills " + name + ". R.I.P.")
            print("Game over.")
            time.sleep(5)
            game_over()
    # And lastly, some basic fluff to cover less common scenarios.
    elif (strength - enemy_defense) < 0:
        print(name + " attacks " + enemy_name + " but does no damage!")
    else:
        print(enemy_name + " attacks but is blocked!")
    # And loop back to the battle_handler function at the end.
    battle_handler()

# And last but not least for entire functions: The game over function.
# There's not a lot of complexity here so go ahead and just copy it as needed


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


enemy_name_options = ["Bob", "Tim", "George", "Bigg", "Lil'", "The great", "Spid", "Kay", "Aaron", "Phillip",
                      "Korrin", "David", "Kieran", "Cassandra", "Daniel", "Jesus", "Adam", "Jessica", "The great big", "Sir Benedict"]
enemy_surname = ["Kurpshank", "Smellwich", "Landar", "Dick", "Spork", "Kumkwat", "Beardsly",
                 "The angry", "The depressed", "The violent", "McLeary", "Goth", "Jenkins", "Monarch of RPyG", "Jowels"]

# Finally, for the cases wherein someone sequence breaks somehow, just send them back to the intro()
intro()

# To finish up, just hook battle_handler into...
# And the name_selector into...

# Ta-Da! You've just written a game in python! 
# *This isn't a game development course AND we used some patterns and techniques that really aren't recommended.
# This particular lesson was more heavily focused on applying core python concepts in a fun and simple way.