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

    print(f"You made it through, however {suspicion} guards were alerted")
    print("")
    time.sleep(2)

    if choice>4:
        if code>=500 and code<=999:
            clue = -2
        elif code>=100 and code<=499:
            clue = -1
    else:
        clue = (code//100)


    return suspicion, clue

def side_room(investigate, code):
    """function that will prompt the player if they want to search an extra side room (more risk more reward)"""
    chance = random.randint(0,100) # random variable that dictates clues and suspicion
    suspicion = (chance+1)//20
    rightmost=code%10
    print("You chose to investigate the room")
    time.sleep(2)
    print("")
    print("Inside the room lays what used to be a lab, shattered test tubes, damaged equipment, toppled workstations, fluorescent lights hanging by a wire from the ceiling, and signs of futile struggle mark the floor")
    time.sleep(5)
    print("")
    print("You begin searching the scattered cabinets...")
    time.sleep(2)
    print("")
    if chance >81:
        print(f"you managed to find a wrinkled lab note, the bottom half reads: 'Don't Forget! The full code is {code}'")
        print("")
        print("----------")
    elif chance>31 and chance<80:
        print(f"You find a clue, the rightmost digit of the code is {rightmost}")
        print("")
    elif chance<=31:
        print("You search, but cannot find anything in time, you leave the laboratory empty-handed.")
        print("")
        print("----------")

    return suspicion, code

def crack_code(suspicion, code):
    """the big moment where the player must crack open the safe containing the bioweapon"""
    guess = 0
    print("You sneak through the seemingly abandoned facility, but something doesnt sit right... so you remain stealthy")
    print("")
    time.sleep(3)
    print("Finally you find the vault, unguarded, so you take your chance")
    print("")
    attempts = 10-suspicion
    while attempts != 0:
        print(f"You have time for {attempts} attempt(s)")
        print("")
        guess = int(input("Enter code: "))
        if guess != code:
            print("")
            print("---Incorrect---")
            print("")
            suspicion+=1
            attempts-=1
            success = False
        elif guess == code:
            print("The safe creaks open...")
            time.sleep(2)
            print("")
            print("Empty")
            success = True
            break
    print("Agent, our sensors have detected multiple anomalous heat signatures within the facility, LEAVE IMMEDIATELY.")
    time.sleep(3)
    print("")
    print("those werent guards to begin with")
    return suspicion, success

def escape(suspicion):
    """the final scene where the player must make a run for it and escape the facility"""

def heist():

    suspicion = 0 #initializing the suspicion counter for the main game, not associated with the normal "suspicion" counter in the functions

    code = random.randint(100, 999)
    if DEBUG==True:
        print(f"DEBUG CODE: {code}")
##Player greeting and entry scene
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

    choice = int(input("Choose a method of entry "))

    while True:
        if choice <1 or choice>6:
            print("Invalid choice, try again")
            print("")
            choice = int(input("Choose a method of entry "))
        else:
            break
    print("")

    suspicion, clue = entry(choice, code)

    if clue == -1:
        print("After sneaking around abandoned labs workstations and quiet halls, you piece together that the code is between 100 and 499")
    elif clue== -2:
        print("Europas laboratory groans under the stress of its ocean currents, despite that you managed to put together that the code for the vault is between 500 and 999")
    else:
        print(f"Despite the wasteland of a laboratory, the scientists were kind enough to leave behind a torn sticky note with the first digit for the vault code being {clue}")
    print("")
    print("----------")
    print("")
    print(f"Dont get your hopes up just yet, this is only the beginning.")
    print("")
    print(f"--Suspicion: {suspicion}")

    print("")
    print("----------")
    print("")
    investigate=None
    while True: # this loop is created to make the player only choose yes or no
        investigate = input("You spot a room on the side, you investigate a side room? (y/n) ")
        if type(investigate)!= str:
            print("Invalid option, try again")
        if investigate=="y":
            suspicion, clue = side_room(investigate, code)# assigns updated suspicion and clue variables after calling the side-room function
            break
        elif investigate=="n":
            print("You chose to ignore the room")
            break
        else:
            print("Invalid option, try again")
    crack_code(suspicion, code)

##end of functions

print_signature()

heist()