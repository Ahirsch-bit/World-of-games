def load_game():
    # user can choose either a number between 1 and 3 or type the game name.
    game_choice = input("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    
    If you do not wish to play anymore, simply type 'end'. """)
    if "memory" in game_choice.lower():
        return "1"
    if "guess" in game_choice.lower():
        return "2"
    if "currency" in game_choice.lower():
        return "3"

    return game_choice


class Setup:

    def __init__(self):
        self.name = input("Please enter your name.")

    def welcome(self):
        print(f"Hi {self.name}, and welcome to World of Games (WoG)! Here you can find many cool games to play.")

    def goodbye(self):
        print(f"Thank you for playing with us, {self.name}. I hope to see you again some time.")
