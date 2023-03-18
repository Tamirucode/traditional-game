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

    def result_check(self, player, computer):
        """
        just print the player score by judging the game win,loss and tie
        has no return
        """
        # using conditional statement to implement the logic

        if player == computer:
            self.ties += 1
            print("The game is a tie! no one win!")
        elif (player - computer) % 3 == 1:
            self.wins += 1
            print("You win!")
        else:
            self.losses += 1
            print("you lose!")
        
    def display_score(self):
        """
        it shows the player score against the computer.
        has no return, it prints the player result
        """
        print(f"You have {self.wins} wins, {self.losses} losses, and "
              f"{self.ties} ties.")
    
    def run_game(self):
        """
        player Plays a round of Rock-Paper-Scissors with the computer.
         function has no return
        """
        while True:
            # try statements created to ensure valid input entered.
            try:
    # using only number input because much easier the user to play the game
                player = int(input('Please enter your choice as a number\n'
                                   '(rock = 0, paper = 1, scissors = 2):\n'))
                if 2 >= player >= 0:
                    break
            except ValueError:
                print('You provided not a number, please enter valid number!')
            else:
                print('Number should be between 0 to 2, please try again!')
    