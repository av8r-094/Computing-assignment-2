"""This file describes documentation standards for ENG 1P13.

Every python file should start with a docstring header like this one. It
should contain your name, student number, and a short description of the
purpose of the program.

Sam Scott, McMaster, 2025"""

## Constants
# Constants are variables with values that should not change
# By convention, we define constants at the top and name them with ALL CAPS
# Use constants to make a program configurable and readable

EXPONENT = 5 #needs some explanation


## Variable Names
# The variable  names below are no good.
# Variables should have meaningful names like user_age or
# compute_mean_population, and should start with a lowercase letter

bbb = 3 # don't use cryptic variable names
UserAge = 20 # don't start with a capital letter
user_age = 20 # much better!

## Header Comments
# use header comments like the one above to mark sections of code in Pyzo
# For example, Input, Processing, Output might have separate sections

## Single-Line or Tag Comments
# use tag comments to explain anything that's not obvious

print("hello") # this is too obvious to comment

amount = 99.99
i = 10
price = 23.7 + amount / i ** EXPONENT   # this might need some explanation!

## Functions
def example_function(first_parameter, second_parameter): # acceptable file header
    """Every function should also have a docstring like this one, placed
    between the function header and the code. Give a one line description
    of the function and describe its parameters, return value, and
    outputs."""

def DoTheThing(y,z,a): #unacceptable file header
    """Functions should have meaningful names, like compute_mean.
    Parameters and variables should also have meaningful names like
    mean_population and user_age. Functions and parameter names should
    also start with lowercase letters. Function headers like the one on
    this function are not acceptable"""
