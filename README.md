
##   overview 
 
Rock Paper Scissors game is a python terminal game running in the code institute mock terminal Heroku.
The terminal-based game hopes to show how the python concept works in-game applications.  
It will be targeted toward adults and children, to have fun with. It will allow truly fair random play between two people.

![mock_imape_Heroku app](https://user-images.githubusercontent.com/116649197/226162114-5e931b52-106d-4d75-a2c3-803ad8970201.png)


##  How to play
Rock Paper Scissors game is a hand game, usually played between two player.You can read more about.[Wikipedia](https://en.wikipedia.org/wiki/Rock_paper_scissors) 

In this game architecture, the game is between'x'player and the computer. First, the player enter their name. then the player enter only one number choice with corresponding list options if wanted play rock choice must be 0, similarly paper choice must be 1 and finaly wanted to play scissors choice must be 2. The computer randomly will chosen one of these three integers.
The winner is 
 - if 'x' player decides to play rock will beat the computer choice scissors, but 'x' player will lose when the computer choice paper.
 - if 'x' player decides to play paper will beat the computer choice rock, but 'x' player will lose when the computer choice scissors.
 - if the 'x' player decides to play scissors will beat the computer choice paper, but 'x' player will lose when the computer choice rock.
 - if both players choose the same shape(in my context the same numbers) the game is tied, so no one will win. They will play again. 
 ##   Features 
	
  - Existing features
       - Randomly generated game
          - choices are randomly placed on computer side.
          - The player can't see what the computer intended to choose ,
       - The Game type and Player Name
       
 ![name_gametype_terminal](https://user-images.githubusercontent.com/116649197/226162485-3ee14007-c36c-43a1-90f6-69bc44fd4b56.png)
          
	  - At the top of the terminal, the command line shows welcome a message to 
              the player shows the game type: Rock paper scissors, it tells the user 
          - what type of game he is playing. Also, player name has seen in the 
               command line, making it easier to know who is playing against the computer.

           - play against the computer
           - accept user input
	   - shows who wins between the players
    - Input validation and error checking 
       - you cannot enter input outside number
       - you cannot provide number outside limit range				
       - you cannot enter negative numbers , only postive integer

![input_validation_my Git pod terminal](https://user-images.githubusercontent.com/116649197/226163350-26a53051-29de-43d7-8758-8c97255c45eb.png)
![validation_terminal](https://user-images.githubusercontent.com/116649197/226162983-406debf5-4fa8-4eec-8bd1-1a66609e9e6d.png)
         
          - play the game
             - user continue playing the game must enter the 'y' letter either 
              lower or upper case, user input outside this letter is not accepted.

![play_again](https://user-images.githubusercontent.com/116649197/226163018-bf87cefb-41ef-44f4-9908-4de08a4b7d43.png)
          
	  - exit game
	      -user wanted stop playing the game must enter 'n' letter in 
               either case, user input outside this letter is not accepted.

![exit_game validation_terminal](https://user-images.githubusercontent.com/116649197/226162367-8f0eddb1-3f02-4135-bcdb-29556b89bb8d.png)
	

## Future Features
			
- when there is time, I would like to extend the traditional game rock paper scissors 
    by adding two options namely 'spock' and 'lizard' from The Bing Bang Theory.
			
## Data Model

- I intended to use rock paper scissors class as my model. The game creates two instance
    of class to hold  the player and the computer side.
- classes (data model) store, the number of wins, losses, and ties, the player against the computer.
- The class also methods to help play the game, such as random_choice method to add alternatives to computer side 
   and display method to add new game to the player and return result.

## Testing
   - I have mannually test this project by doing the following
    - below generate tested values screen shot  from my local and code institute Heroku terminal
      presented:-
      - by supplied invalid inputs:- strings when number is expected,
       negative number when positve integer expected, outside defined limit.
    - passed the code through a PEP8 linter and confirmed there are no
      problem.			

![continued_exit validation terminal](https://user-images.githubusercontent.com/116649197/226162822-4caa348c-2ffe-4422-8855-ffa4278607ef.png)
![continued_validation_Heroku terminal](https://user-images.githubusercontent.com/116649197/226162836-bf010ad7-eb82-4b64-a242-51ac81b326b4.png)
![continued_validation_Heroku_terminal](https://user-images.githubusercontent.com/116649197/226162849-c5bf2916-fc89-45b1-b688-4b1460df4e13.png)
![input validation_terminal](https://user-images.githubusercontent.com/116649197/226162724-84b3c8c2-ff99-41b5-86b7-d3975e3fa453.png)
![input validation_terminal](https://user-images.githubusercontent.com/116649197/226162456-a1eaf1ee-265a-4d61-9129-e90a537f6116.png)
![continued_exit validation terminal](https://user-images.githubusercontent.com/116649197/226162165-b55bfb52-586a-4b22-a4c6-dd8e93754cc6.png)	

## Validator Testing
  - PEP8			
	  - No errors were returned from PEP8online.com
## Bugs
  - Solved bugs
      - when I tested the input validator to continue playing the game, i was getting it accepts any type of input. 
        I fix this by adding if statemenets.
  - Remaining bugs
	  - no bugs 

## Deployment
 - The site was deployed to GitHub pages and code institute Heroku terminal.
1. navigate Heroku  dashboard page  then click setting tab
2. In my case no need config vars. then go to add buildpack by clicking its tab
3. next select the first python,second noodjs and save changes.
4. After  that go Heroku dashboard page  then click deploymnet tab
5. just click Github then connect and confirm connect Github
6. Type in the blank box my repository,traditional-game and click search
7. click connect buttton to connect Heroku app
8. scroll down the page click deploy branch and the app being built
9. Finally,we see deployement the app successful message and
10. click the view button to take a look
- The live link can be found here:- [traditional-game](https://traditional-play.herokuapp.com/)

## Cloning a repository
 1. navigate the desktop version Github Dashboard 
    open file menu, click clone Repository
 2. then click the location of the repository, 
 3. From the list of repository, click traditional-game
 4. select local directory and file path
 5. finaly, click to clone traditional-game.
## Technology Used
   - python
## Frameworks, Library and Program
1. python module
   - import random
2. Git
   - used Git terminal to commit to Git and push to Git hub
3. GitHub
4. Heroku
   - store the project code after being pushed from Git

## Credits
   - Code
      - From youtube tutorial to implement the python if statement code line 86
        to do the game running round, code run inside that fuction and exit() code line 105
        to close the game
        https://www.youtube.com/watch?v=3ppJt87QPNg
      - MDN web docs
      - love sandwiches 
      - From youtube tutorial has got some information how to design the game 
       https://www.youtube.com/watch?v=XnoXEUQrIM8
      - I received some help from my fellow student 
   - content
	   - The content is written by developer





