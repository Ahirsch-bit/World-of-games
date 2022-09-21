import time
from abc import ABC


def check_validity(x):
    if not x.isdigit():
        return False
    else:
        num = int(x)
        if num > 5 or num < 1:
            return False
        else:
            return True


class BaseGames(ABC):
    # In order to avoid making an instance of "base games", I have made the class abstract.
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.difficulty = input("Please choose game difficulty from 1 to 5: ")
        is_valid = check_validity(self.difficulty)
        while not is_valid:
            self.difficulty = input("The options are only between 1 and 5. This should not be that hard. Please "
                                    "choose a number between 1 and 5.")
            is_valid = check_validity(self.difficulty)
        super(BaseGames, self).__init__()

    def load_game(self):
        print(f"Thank you for choosing to play {self.__class__.__name__}. You are playing with difficulty "
              f"level {self.difficulty}.")

    def check_results(self, game):
        if game:
            print("Wow! You are correct. That was amazing!")
            self.score = int(self.difficulty) * 3 + 5
        else:
            print("Too bad. Better luck next time!")

    def end_game(self):
        print(f"That was fun, {self.name}. Let's do this again sometime.")
        print("You will now be sent back to the main screen.")
        print(f"A total of {self.score} points will be added to your score.")
        time.sleep(2)
        return self.score
