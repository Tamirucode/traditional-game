##   overview 
 
Rock Paper Scissors game is a python terminal game running in the code institute mock terminal Heroku. The terminal-based game hopes to show how the python concept works in-game applications.  
It will be targeted toward adults and children, to have fun 
with. It will allow truly fair random play between two people.

##  How to play
Rock Paper Scissors game is a hand game, usually played between two player.You can read more about.Wikipedia 

In this game architecture, the game is  between'x'player and the computer. First, the player enter their name. then the player enter only one number choice with corresponding list options if wanted play rock choice must be 0, similarly paper choice must be 1 and finaly wanted to play scissors choice must be 2. The computer randomly will chosen one of the three integers.
The winner is 
		- if 'x' player decides to play rock will beat the computer choice scissors, but 'x' player will lose when the computer choice paper.
		if 'x' player decides to play paper will beat the computer choice rock, but 'x' player will lose when the computer choice scissors.
		if the 'x' player decides to play scissors will beat the computer choice paper, but the 'x' player will lose when the computer choice rock.
		if both players choose the same shape(in my context the same numbers) the game is tied,so no one 
        will win. They will  play again. 
 ##   Features 

		Existing features
	
	         ** The Game type and Player Name 
			    At the top of the terminal, the command line interface shows welcome a message to 
                the player shows the game type: Rock paper scissors, it tells the user 
                what type of game he is playing. Also, player name has seen in the 
                command line, making it easier to know who is playing  with the computer.
            
            
                - play against the computer
			    - accept user input
			    - shows who wins between the players


                - Input validation and error checking 
				    - you cannot enter input outside number
				    - you cnnnot provide number outside limit range				
                    - you cannot enter negative numbers , only postive integer 
                -play the game
                    -user continue playing the game must enter the 'y' letter either 
                    lower or upper case, user input outside this letter is not accepted.
                -exit game
			        *user wanted stop playing the game must enter 'n' letter in 
                     either case, user input outside this letter is not accepted.


## Feature Features
			
- when there is time, I would like to extend the traditional game rock paper scissors 
    by adding two options namely  'spock' and 'lizard' from The Bing Bang Theory.
			
## Data Model

- I intended to use rock paper scissors class as my model. The game  creates  two instance
    of class to hold  the player and the computer side.
- classes (data model) store, the number of wins, losses, and ties, the player against the computer.
- The class also methods to help play the game, such as random_choice method to add alternatives to computer side and print method to add new game to the player and return result.


