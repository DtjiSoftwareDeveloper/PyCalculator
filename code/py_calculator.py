"""
This file contains code for the application "PyCalculator".
Author: DtjiSoftwareDeveloper
"""


# Importing necessary libraries

import sys
import os
from mpmath import *

mp.pretty = True


# Creating static functions.


def sin(mp_num: mpf):
    return mp.sin(mp_num)


def cos(mp_num: mpf):
    return mp.cos(mp_num)


def tan(mp_num: mpf):
    return mp.tan(mp_num)


def asin(mp_num: mpf):
    return mp.asin(mp_num)


def acos(mp_num: mpf):
    return mp.acos(mp_num)


def atan(mp_num: mpf):
    return mp.atan(mp_num)


def sinh(mp_num: mpf):
    return mp.sinh(mp_num)


def cosh(mp_num: mpf):
    return mp.cosh(mp_num)


def tanh(mp_num: mpf):
    return mp.tanh(mp_num)


def asinh(mp_num: mpf):
    return mp.asinh(mp_num)


def acosh(mp_num: mpf):
    return mp.acosh(mp_num)


def atanh(mp_num: mpf):
    return mp.atanh(mp_num)


def clear():
    # type: () -> None
    if sys.platform.startswith('win'):
        os.system('cls')  # For Windows System
    else:
        os.system('clear')  # For Linux System


# Creating main function used to run the application.


def main():
    """
    This main function is used to run the application.
    :return: None
    """

    print("Welcome to 'PyCalculator' by 'DtjiSoftwareDeveloper'.")
    print("In this application, you will be able to write your equation and it will print the output.")
    print("Notes: All trigonometric functions (e.g. sin and cos) will take radians as the parameter.")
    print("So, sin(mp.pi / 2) = 1")

    # Asking the user whether he/she wants to do a calculation or not.
    print("Enter 'Y' for yes.")
    print("Enter anything else for no.")
    do_calculation: bool = input("Do you want to do a calculation? ") == "Y"
    while do_calculation:
        # Clearing the command line window.
        clear()

        # Asking the user to enter an equation.
        equation: str = input(">>> ")

        try:
            # Printing the results of the equation.
            print(eval(equation))
        except ValueError:
            print("ERROR!!!!!")

        # Clearing the command line window.
        clear()

        # Asking the user whether he/she wants to do a calculation or not.
        print("Enter 'Y' for yes.")
        print("Enter anything else for no.")
        do_calculation = input("Do you want to do a calculation? ") == "Y"


if __name__ == '__main__':
    main()
