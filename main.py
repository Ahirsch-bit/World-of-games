from games.CurrencyRoulette import CurrencyRoulette
from games.GuessGame import GuessGame
from games.MemoryGame import MemoryGame
from setup.Live import Setup, load_game

game = Setup()
game.welcome()

game_choice = load_game().lower()

while game_choice != 'end':
    match game_choice:
        case "1":
            MemoryGame(game.name).memory_game()
        case "2":
            GuessGame(game.name).guess_game()
        case "3":
            CurrencyRoulette(game.name).currency_roulette_game()
        case _:
            print("This is not a valid option. Please choose an option between 1 and 3. ")
    game_choice = load_game().lower()

game.goodbye()
