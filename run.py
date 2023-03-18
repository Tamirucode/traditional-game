# Import needed data libraries--
import random
print("______________________________________________\n")
print("Welcome to Rock Paper Scissors Game!!\n ")
print("----------------------------------------------\n")
# ---using the code below just to know who is playing with the computer.
x = input("Please enter your name: \n")
print("----------------------------------------------\n")
player = x

class RockPaperScissors:
    """
    Class to handle an instance of a Rock-Paper-Scissors game
    """

    def __init__(self):
    """
        Initialize the variables for the class
        """
        