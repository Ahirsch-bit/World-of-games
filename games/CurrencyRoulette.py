import random

from games.BaseGames import BaseGames
from forex_python.converter import CurrencyRates


class CurrencyRoulette(BaseGames):
    def play(self):
        self.load_game()
        usd_amount = random.randint(1, 100)
        interval = self.get_money_interval(usd_amount)
        guess = self.get_guess_from_user(usd_amount, interval)
        self.check_results(guess)
        self.end_game()

    def get_money_interval(self, num):
        c = CurrencyRates()
        rate = 1 / c.get_rate('ILS', 'USD')
        amount = num * rate
        return [amount - (5 - int(self.difficulty)), amount + (5 - int(self.difficulty))]

    def get_guess_from_user(self, num, num_range):
        guess = input(f"Guess the amount of {num}USD in shekels, within {5 - int(self.difficulty)} shekels.")
        if not guess.isdigit():
            return False
        else:
            guess_float = float(guess)
            if num_range[0] <= guess_float <= num_range[1]:
                return True
            else:
                return False
