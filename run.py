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
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.alternatives = {'rock': 0, 'paper': 1, 'scissors': 2}
    
    def random_choice(self):
        """
        The computer choice from list of self.alternatives.
        return the dictionary values of rock= 0 , paper = 1
        and scissors = 2.
        """

        return random.choice(list(self.alternatives.values()))
    