# World-of-games
For DevOps course project

### How to play: ###

Gameplay is quite simple. Clone the project and run from main. The game will basically
ask for your name and give you 3 game options. and up to 5 difficulty levels.

Once a game is completed, you will be redirected to the main menu and be given the option
to play another game. From the main menu, you can exit the program by simply typing 'end'.

There will be a running tally of the scores for each game under each player, and it will
constantly be updated. In addition, there is a Flask app which generates a website that displays
the scores. The Flask app has two endpoints. One is a REST API call which returns the JSON object
with the scores, and the other one is to host the HTML file for the website. 


