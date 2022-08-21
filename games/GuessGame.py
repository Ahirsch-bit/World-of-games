import random

# Ideally I would have combined a few of these methods, as they are quite small,
# but the requirements specified specific methods with specific method names.
from games.BaseGames import BaseGames


def get_guess_from_user(num):
    guess = input(f"Choose a number between 1 and {num}.")
    return guess


def compare_results(num, guess):
    if not guess.isdigit():
        return False
    else:
        guess_int = int(guess)
        if guess_int == num:
            return False
        else:
            return True


class GuessGame(BaseGames):

    def play(self):
        self.load_game()
        num = self.generate_number()
        guess = get_guess_from_user(num)
        compare = compare_results(num, guess)
        self.check_results(compare)
        self.end_game()

    def generate_number(self):
        return random.randint(1, int(self.difficulty))
