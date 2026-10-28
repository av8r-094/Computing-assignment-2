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


    return (f"You broke in! However {suspicion} Guards were alerted, the leftmost digit for the code is {clue}")

#entry function ends here

def side_room(investigate, code):
    """function that will prompt the player if they want to search an extra side room (more risk more reward)"""
    chance = random.randint(0,100) # variable that randomly decides if the player will get the full code or the rightmost digit
    rightmost=code%10
    if chance >81:
        print(f"Lucky! the full code is {code}")
    elif chance>31 and chance<80:
        print(f"Nice try, the rightmost digit of the code is {rightmost}")


#side_room function ends here


def crack_code(investigation, code):
    """the big moment where the player must crack open the safe containing the bioweapon"""

#crack_code functions ends here

def escape(suspicion):
    """the final scene where the player must make a run for it and escape the facility"""

# escape function ends here


print_signature()



def heist():
    code = random.randint(100, 999)
    if DEBUG==True:
        print(code)


    choice = float(input("Choose a method of entry "))
    print(entry(choice,code))
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




heist()