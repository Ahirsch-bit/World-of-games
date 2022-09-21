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
        self.name = input("Please enter your name.").strip()

    def welcome(self, score):
        print(f"Hi {self.name}, and welcome to World of Games (WoG)! Here you can find many cool games to play.")
        if score == 0:
            print("It looks like this is your first time playing with us. I hope you enjoy it!")
        else:
            print(f"It's great to have you back! Your current all time score is {score}")

    def goodbye(self, score_initial, score_final):
        if score_initial == 0:
            print("I can see that you didn't earn any points this time. "
                  "Since we really enjoyed playing with you, please take 3 points for your troubles.")
        print(
            f"During this session you accrued {score_initial} points. This will be added to your previous score "
            f"of {score_final}. "
            f"Thank you for playing with us, {self.name}. I hope to see you again some time.")
