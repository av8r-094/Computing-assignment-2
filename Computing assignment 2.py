"""Computing 2 assignment: the Big Heist
this computing assignment is a game about breaking into a secure facility on Europa, one of Jupiters moons to steal a bioweapon

Created by Ioannis(John) Zografos - 400680100, 2026"""

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

    print(f"You made it through, however {suspicion} guard(s) were alerted")
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
    suspicion = 0
    clue = -1
    if investigate=="y":
        chance = random.randint(0,100) # random variable that dictates clues and suspicion
        suspicion = (chance+1)//20
        rightmost=code%10
        print("Inside the room lays what used to be a lab, shattered test tubes, damaged equipment, toppled workstations, fluorescent lights hanging by a wire from the ceiling, and signs of futile struggle mark the floor")
        time.sleep(5)
        if chance >=81:
            clue = code
        elif chance>=31 and chance<=80:
            clue = rightmost
        elif chance<=31:
            clue = -1
    else:
        print("You ignore the room")

    return suspicion, clue

def crack_code(suspicion, code):
    """the big moment where the player must crack open the safe containing the bioweapon"""
    guess = 0
    attempts = 10-suspicion
    print(f"You have time for {attempts} attempts")
    for i in range(attempts):
        guess = math.floor(float(input("Enter 3-digit code: ")))
        if guess == code:
            print(f"Attempt {i+1}: Guess = {guess}, ---Correct---")
            success = True
            return suspicion, success
        else:
            print(f"Attempt {i+1}: Guess = {guess}, ---Incorrect---")
            success= False

    return suspicion, success

def escape(suspicion):
    """the final scene where the player must make a run for it and escape the facility"""
    danger = suspicion//3
    progress = 0
    accepted_inputs = ("Run", "Hide", "Shortcut")

    while True:
        if progress >= 10 or danger >=10:
            break

        inpt = input("Choose action: Run, Hide or Shortcut - ")
        while inpt not in accepted_inputs:
            print("Invalid choice, try again")
            inpt = input("Choose action: Run, Hide or Shortcut - ")
        det = random.randint(1,100)
        if inpt =="Run" and det<=60:
            progress+=1
            print(f"You lost them, but theyre still searching. Progress = {progress}, Danger = {danger}")
        elif inpt =="Run" and det>60:
            danger+=1
            progress+=1
            print(f"You run but theyre still tailing you. Progress = {progress}, Danger = {danger}")
        elif inpt=="Hide" and det<=80:
            print(f"They pass by you as you hide in a crevice. Progress = {progress}, Danger = {danger}")
        elif inpt=="Hide" and det>80:
            print(f"Your hiding attempt was futile. Progress = {progress}, Danger = {danger}")
            danger+=2
        elif inpt=="Shortcut" and det<=50:
            progress+=3
            print(f"You jump into the vents and sneak away successfully. Progress = {progress}, Danger = {danger}")
        elif inpt=="Shortcut" and det>50:
            danger+=3
            print(f"You try to sneak away but the change in your pocket falls out and alerts the entities. Progress = {progress}, Danger = {danger}")

    return progress

def heist(name):

    retry = True #initializes the retry variable, which will change if the palyer chooses to play again

    suspicion = 0 #initializing the suspicion counter for the main game, not associated with the normal "suspicion" counter in the functions

    while retry == True:

        code = random.randint(100, 999)
        if DEBUG==True:
            print(f"DEBUG CODE: {code}")
##Player greeting and entry scene
        print(f"Greetings {name}, you are summoned here today on behalf of the Intergalactic Erusian Task Force.")
        time.sleep(3)
        print("A rogue privately funded military has been developing a Bioweapon on one of Jupiters moons; Europa, and its capable of exterminating life as we know it.")
        time.sleep(4)
        print("Your task: Break into their vault and make it out alive with the Bioweapon")
        time.sleep(3)
        print("Entry points:")
        print("1. Surface Hatch")
        print("2. Emergency exit")
        print("3. 2nd Emergency exit")
        print("4. Launchpad hatch")
        print("5. SkyLight")
        print("6. Underwater Hatch (Submarine)")
        time.sleep(4)
        print(f"Remember {name}, the easier the entry, the higher the chance that guards will be alerted, stay vigilant")
        choice = int(input("Choose a method of entry "))
        while True:
            if choice <1 or choice>6:
                print("Invalid choice, try again")
                choice = int(input("Choose a method of entry "))
            else:
                break
        suspicion_e, clue = entry(choice, code)
        suspicion+=suspicion_e #adds suspicion gained from entry scene
        if clue == -1:
            print("After sneaking around abandoned labs workstations and quiet halls, you piece together that the code is between 100 and 499")
        elif clue== -2:
            print("Europas laboratory groans under the stress of its ocean currents, despite that you managed to put together that the code for the vault is between 500 and 999")
            time.sleep(4)
        else:
            print(f"Despite the wasteland of a laboratory, the scientists were kind enough to leave behind a torn sticky note with the first digit for the vault code being {clue}")
##Side room scene
        inputs = ("y", "n")
        investigate = input("You spot a peculiar room, do you investigate? (y/n)")
        while investigate not in inputs:
            investigate = input("Invalid input, try again:")
        suspicion_s, clue = side_room(investigate, code)
        suspicion+=suspicion_s
        if clue==-1 and investigate=="y":
            print("Despite thoroughly searching the room, you leave empty handed")
        elif clue!=-1 and investigate=="y":
            print(f"You find a note on the desk, the rightmost digit of the 3-digit code is {clue}")
        time.sleep(3)
        print("You sneak through the rubble within the facility, but something doesnt sit right...")
        time.sleep(3)
        print("You spot the battered vault, and take the chance to try and open it")
##Cracking the code scene
        suspicion_c, success = crack_code(suspicion, code)
        suspicion+=suspicion_c #adds suspicion gained from code scene
        if success==True:
            print("You open the vault, to nothing!!")
        else:
            print("You did not manage to open the vault in time.")
        print("Your radio starts hissing with static and you hear multiple heavy footsteps, you dont know what those things are and youre not going to find out")
##Escape scene
        progress = escape(suspicion)
        if progress>=10:
            print("You did what you could, but the things you learned in that lab will haunt you.")
            time.sleep(4)
        elif progress<10:
            print("You fail to return home, and the events of what happened on Europa remain unknown")
##Retry inquiry
        redo = input("Would you like to play again? (y/n)") # the variable redo will dictate if the variable retry is true or false which will determine if the game runs again from the beginning
        accepted_inputs2 = ("y", "n")#2nd variable that determines the accepted inputs, in this case to determine if the game will end or replay from the beginning
        while redo not in accepted_inputs2:
            print("Invalid option.")
            redo = input("Would you like to play again? (y/n)")
        if redo=="y":
            retry=True
        elif redo=="n":
            retry = False

##end of functions

print_signature()

name = input("Before we begin, enter your name: ")

heist(name)

print(f"Thank you for playing my game {name}")