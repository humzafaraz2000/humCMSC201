# File: proj1.py
# Author: Humza Faraz
# Date: 10/24/18
# Section: 19
# E-mail: hfaraz1@umbc.edu
# Description: Adventure game where user must survive 7 nights or escape
#              from the Demegrogan

from random import randint, seed
seed(100)

#constants for player and monster health
MAX_HEALTH = 100
MIN_HEALTH = 0

DEM_MAX_HEALTH = 300

#constants for survival
SURVIVE_DAYS = 7
SURVIVE_DIST = 150

#constants list for food and items
FOODS = ["Reese's Pieces", "Pop Rocks", "Ovaltine", "Wonder Bread", "Twinkies"]

ITEMS = ["Sword", "Bicycle", "Hi-C", "Heelys",
         "Walkman", "Laser Cannon", "Rubber Band"]

#current state of mutable values
fight = False
camp = False
equippedItem = "N/A"
inventory = ["Walkie talkie", "Flashlight"]

#getUserChoice() asks the user to select a choice from a list of choices
#                continuously prompts the user until the choice is valid
#                a valid choice is one that is a valid index in the list
#Input:          choices; a list of all possibble choices available
#Output:         choice; the validated choice that the user made
def getUserChoice(choice):
    choice = int(input("Your options are: \n1 - View inventory \
                        \n2 - View current stats \n3 - Eat an eggo waffle \
                        \n4 - Nothing else. \nEnter a choice: "))
    while (choice > 4 or choice < 1):
        print ("Invalid choice.")
        choice = int(input("Your options are: \n1 - View inventory \
                            \n2 - View current stats \n3 - Eat an eggo waffle \
                            \n4 - Nothing else. \nEnter a choice: "))
    if (itemChoice == 1):
        itemSelection = input("Enter item you'd like to equip: ")
        equippedItem = itemSelection
    elif (itemChoice == 2):
        itemRemoval = input("Enter item you'd like to unequip:")
        equippedItem = "N/A"
    else:
        print ("Okay that's fine.")
   
    return choice

#def displayChoice() Prints the user's options
def displayMenu(playerHealth, distance, equippedItem, inventory):
    waffle = 0
    choice = int(input("Your options are: \n1 - View inventory \
                        \n2 - View current stats \n3 - Eat an eggo waffle \
                        \n4 - Nothing else. \nEnter a choice: "))
    while (choice < 4):
        if (choice == 1):
            print ("Your inventory",inventory)
            print ("Would you like to equip an item?\n1 - Equip item\n2 - Unequip item\n3 - Nevermind")
            itemChoice = int(input("Enter choice: "))
            if (itemChoice == 1):
                itemEquip = input ("Enter item you'd like to equip: ")
                equippedItem = itemEquip
                choice = int(input("What else would you like to do? \n1 - View inventory \n2 - View current stats \
                                    \n3 - Eat an eggo waffle \n4 - Nothing else" ))
            elif (itemChoice == 2):
                print ("You unequipped",equippedItem)
                equippedItem = "N/A"
                choice = int(input("What else would you like to do? \n1 - View inventory \n2 - View current stats \
                                    \n3 - Eat an eggo waffle \n4 - Nothing else" ))
            else:
                print ("Ok that's fine.")
                choice = int(input("What else would you like to do? \n1 - View inventory \n2 - View current stats \
                                    \n3 - Eat an eggo waffle \n4 - Nothing else" ))
        elif (choice == 2):
            print ("Current health:", playerHealth)
            print ("Distance traveled",distance)
            print("Equipped item:",equippedItem)
            choice = int(input("What else would you like to do? \n1 - View inventory \n2 - View current stats \
                                \n3 - Eat an eggo waffle \n4 - Nothing else" ))
        elif (choice == 3):
            if (waffle == 0):
               if (playerHealth < (MAX_HEALTH - 10)):
                  print("You ate a waffle. So bad, yet so good") 
                  health += 10
                  waffle += 1
                  choice = int(input("What else would you like to do? \n1 - View inventory \n2 - View current stats \
                                     \n3 - Eat an eggo waffle \n4 - Nothing else" ))
               elif (playerHealth == MAX_HEALTH):
                   print ("You already have max health!")
                   choice = int(input("What else would you like to do? \n1 - View inventory \n2 - View current stats \
                                       \n3 - Eat an eggo waffle \n4 - Nothing else" ))
               else:
                  health = MAX_HEALTH
                  waffle += 1
                  choice = int(input("What else would you like to do? \n1 - View inventory \n2 - View current stats \
                                      \n3 - Eat an eggo waffle \n4 - Nothing else" ))
            else:
                print ("You can only eat 1 waffle per day.")
                choice = int(input("What else would you like to do? \n1 - View inventory \n2 - View current stats \
                                    \n3 - Eat an eggo waffle \n4 - Nothing else" ))
    print ("Ok that's fine.")
    return choice

#def eat() Changes user's health based on food eaten
def eat(food, playerHealth):
    if (food == "Reese's Pieces"):
        health -= 30
    elif (food == "Pop Rocks"):
        health -= 5
    elif (food == "Ovaltine"):
        if (health < MAX_HEALTH - 15):
            health += 15
        else:
            health = MAX_HEALTH
    elif (food == "Wonder Bread"):
        if (health < MAX_HEALTH - 25):
            health += 25
        else:
            health = MAX_HEALTH
    else:
        if (health < MAX_HEALTH - 30):
            health += 30
        else:
            health = MAX_HEALTH
#def camp() asks user whether they want to stay at their camp or leave
def camp():
    print("The Demegorgan looms in the distance. Do you leave your camp, or stay?")
    print ("Your options are:")
    print ("1 - Pack up camp and go")
    print ("2 - Stay where you are")
    move = int(input("Enter a choice: "))
    if (move == 1):
        camp = False
    else:
        camp = True

    return camp
#def event() Determines whether random event happens to user or not
def event(camp, distance, inventory, fight, playerHealth):
    if (camp == True):
        chance = randint(1,10)
        if (chance <= 7):
            fight = True
        else:
            print ("You survived the night.")
            day += 1
            playerHealth = MAX_HEALTH
    if (camp == False):
        num = randint(1,10)
        if (num <= 2):
            find = randint(1,10)
            if (find <= 2):
                print ("You found",FOODS[0])
                inventory.append(FOODS[0])
                distance = distance + (playerHealth / 4) + 5
                print ("You traveled", distance)
                day += 1
            elif (find <= 4):
                print ("You found",FOODS[1])
                inventory.append(FOODS[1])
                distance = distance + (playerHealth / 4) + 5
                print ("You traveled", distance)
                day += 1
            elif (find <= 6):
                print ("You found",FOODS[2])
                inventory.append(FOODS[2])
                distance = distance + (playerHealth / 4) + 5
                print ("You traveled", distance)
                day += 1
            elif (find <= 8):
                inventory.append(FOODS[3])
                print ("You found",FOODS[4])
                distance = distance + (playerHealth / 4) + 5
                print ("You traveled", distance)
                day += 1
            else:
                print ("You found",FOODS[4])
                inventory.append(FOODS[4])
                distance = distance + (playerHealth / 4) + 5
                print ("You traveled", distance)
                day += 1
        elif (num <= 4):
            item = randint(0,len(ITEMS)-1)
            if (item == 0):
                print ("You found",ITEMS[item])
                inventory.append(ITEMS[item])
                distance = distance + (playerHealth / 4) + 5
                print ("You traveled", distance)
                day += 1
            elif (item == 1):
                print ("You found",ITEMS[item])
                inventory.append(ITEMS[item])
                distance = distance + (playerHealth / 4) + 5
                print ("You traveled", distance)
                day += 1
            elif (item == 2):
                print ("You found",ITEMS[item])
                inventory.append(ITEMS[item])
                distance = distance + (playerHealth / 4) + 5
                print ("You traveled", distance)
                day += 1
            elif (item == 3):
                print ("You found",ITEMS[item])
                inventory.append(ITEMS[item])
                distance = distance + (playerHealth / 4) + 5
                print ("You traveled", distance)
                day += 1
            elif (item == 4):
                print ("You found",ITEMS[item])
                inventory.append(ITEMS[item])
                distance = distance + (playerHealth / 4) + 5
                print ("You traveled", distance)
                day += 1
            elif (item == 5):
                print ("You found",ITEMS[item])
                inventory.append(ITEMS[item])
                distance = distance + (playerHealth / 4) + 5
                print ("You traveled", distance)
                day += 1
            elif (item == 6):
                print ("You found",ITEMS[item])
                inventory.append(ITEMS[item])
                distance = distance + (playerHealth / 4) + 5
                print ("You traveled", distance)
                day += 1
        elif (num <= 6):
            print ("You fell in a trench! You went 1/2 the usual distance and it took you an extra day to get out.")
            distance = (distance + (playerHealth / 4) + 5)/2
            print ("You traveled", distance)
            day += 2
        elif (num <= 9):
            print ("The Demegorgan found you! It's time for a fight!")
            fight = True
        else:
            print ("You survived the day.")
            distance = distance + (playerHealth / 4) + 5
            print ("You traveled", distance)
            day += 1
    return fight, playerHealth, distance, inventory

#calc damage() calculates damage user and Demegorgan deals
def calcDamage(equippedItem, damage):
    damage = 0
    demDamage = 20
    if ("Hi-C" in inventory):
        demHealth = 150
    if ("Walkman" in inventory):
        demDamage = 20*.75
    if (equippedItem == "WalkieTalkie"):
        damage = 10
    elif (equippedItem == "Flashlight"):
        damage = 5
    elif (equippedItem == "Rubber Band"):
        damage = 25
    elif (equippedItem == "sword"):
        damage = 50
    elif (equippedItem == "laser cannon"):
        damage = 100
    return damage, demDamage

#def fight() simulates fight between user and Demegorgan
def fight(playerHealth, equippedItem, inventory,fight):
    if (fight == True):
        print ("The Demegorgan is here! Would you like to fight or run?")
        survive = int(input("1 - Fight\n2 - Flail\n3 - Flee"))
        escape = False
        demHealth = DEM_MAX_HEALTH
        while(escape != True and demHealth != 0):
            if (survive == 1):
                calcDamage(equippedItem, damage)
                playerHealth -= demDamage
                print ("Player Health:",playerHealth)
                print ("Demegorgan Health:",demHealth)
                survive = int(input("Now what?\n1 - Fight\n2 - Flail\n3 - Flee"))
            elif (survive == 2):
                playerHealth = 0
                print ("Your attack is useless and you're killed.")
                print ("GAME OVER")
            else:
                run = randint(1,10)
                if (run <= 30):
                    print ("You escaped!")
                    escape = True
                    day += 1
                else:
                    if ("Walkman" in inventory):
                        playerHealth -= ((20 * .75) * .5)
                        survive = int(input("Now what?\n1 - Fight\n2 - Flail\n3 - Flee"))
                    else:
                        playerHealth -= (20*.5)
                        survive = int(input("Now what?\n1 - Fight\n2 - Flail\n3 - Flee"))
        
def main():
    print ("After miles of hiking in the woods, you finally setup your camp.")
    print ("You decided to go camping on the wrong weekend.")
    print ("Your phone buzzes:\n\tTHE DEMEGORGAN HAS ESCAPED.\tRUN.")

    day = 0
    playerHealth = MAX_HEALTH
    distance = 0
    
    #while user isn't dead and hasn't traveled the max distance
    while (playerHealth > MIN_HEALTH and (distance < SURVIVE_DIST or day < SURVIVE_DAYS)):
        day = 1
        print ("The sun rises on Day",day,"in the forest.")
        print ("\n What would you like to do this morning?")

        #getUserChoice()

        displayMenu(playerHealth, distance, equippedItem, inventory)
        
        camp()

        event(distance, inventory, camp, fight, playerHealth)

        fight(playerHealth, equippedItem, inventory)

    if (day >= SURVIVE_DAYS or distance >= SURVIVE_DISTANCE):
        print ("Congradulations! You win!")
        print ("You survived",day,"days and traveled",distance,"miles.")
    if (playerHealth < MIN_HEALTH):
        print ("GAME OVER. YOU DIED.")
    
main()
