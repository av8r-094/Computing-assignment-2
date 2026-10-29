#Computing 2 assignment: the Big Heist
#this computing assignment is a game about breaking into a secure facility on Europa, one of Jupiters moons to steal a bioweapon





import time
import math
import random

DEBUG = True

def print_signature():
    print("Ioannis(John) Zografos")
    print("400680100, ENG1 CO-OP")
    print("ENG 1P13: Integrated Cornerstone Design Projects in Engineering")
    print("Professor: Dr. Sam Scott (Computing)")
    print("Fall 2026")


def entry(choice, code):
    """entry scene, 3 guards, choice of entry and break-in code are defined here"""
    suspicion = 0 #initiating the suspicion counter
    clue = 0 #initiating clue

    guard1 = random.randint(1,6)
    guard2 = random.randint(1,6)
    guard3 = random.randint(1,6)

    if guard1>choice:
        suspicion = suspicion+1
    if guard2>choice:
        suspicion = suspicion+1
    if guard3>choice:
        suspicion = suspicion+1

    if choice>4:
        if code>=500 and code<=999:
            clue = -2
        elif code>=100 and code<=499:
            clue = -1
    else:
        clue = (code//100)


    return suspicion, clue

#entry function ends here

def side_room(investigate, code):
    """function that will prompt the player if they want to search an extra side room (more risk more reward)"""
    chance = random.randint(0,100) # variable that randomly decides if the player will get the full code or the rightmost digit
    rightmost=code%10
    print("You chose to investigate the room")
    time.sleep(2)
    print("Inside the room lays what used to be a lab, shattered test tubes, damaged equipment, toppled workstations, fluorescent lights hanging by a wire from the ceiling, and signs of futile struggle mark the floor")
    time.sleep(5)
    print("")
    print("You begin searching the scatterd cabinets...")
    time.sleep(2)
    print("")
    if chance >81:
        print(f"you managed to find a wrinkled lab note, the bottom half reads: 'Don't Forget! The full code is {code}'")
    elif chance>31 and chance<80:
        print(f"You find a clue, the rightmost digit of the code is {rightmost}")
    else:
        print("You search, but cannot find anything in time, you leave the laboratory.")

    return suspicion, code
#side_room function ends here


def crack_code(suspicion, code):
    """the big moment where the player must crack open the safe containing the bioweapon"""
    attempts = 10-suspicion
    print("You sneak through the seemingly abandoned facility, but you know someones watching so you remain stealthy")
    print("")
    time.sleep(3)
    print("Finally you find the vault, unguarded, so you take your chance")
    for i in range(attempts):
        print(f"You have time for{attempts-i}")

#crack_code functions ends here

def escape(suspicion):
    """the final scene where the player must make a run for it and escape the facility"""

# escape function ends here


print_signature()



def heist():
    code = random.randint(100, 999)
    if DEBUG==True:
        print(code)

    print("Greetings agent, you are summoned here today on behalf of the Intergalactic Erusian Task Force.")
    print("")
    time.sleep(3)
    print("A rogue privately funded military has been developing a Bioweapon on one of Jupiters moons; Europa, and its capable of exterminating life as we know it.")
    print("")
    time.sleep(4)
    print("Your task: Break into their vault and make it out alive with the Bioweapon")
    print("")
    time.sleep(3)
    print("Entry points:")
    print("1. Surface Hatch")
    print("2. Emergency exit")
    print("3. 2nd Emergency exit")
    print("4. Launchpad hatch")
    print("5. SkyLight")
    print("6. Underwater Hatch (Submarine)")
    print("")
    time.sleep(4)
    print("Remember agent, the easier the entry, the higher the chance that guards will be alerted, stay vigilant")
    print("")

    choice = float(input("Choose a method of entry "))

    investigate=None
    while True: # this loop is created to make the player only choose yes or no
        investigate = input("You spot a room on the side, you investigate a side room? (y/n) ")
        if investigate=="y":
            side_room(investigate, code)
            break
        elif investigate=="n":
            print("You chose to ignore the room")
            break
        else:
            print("Invalid option, try again")
    crack_code(side_room(investigate, code))




heist()