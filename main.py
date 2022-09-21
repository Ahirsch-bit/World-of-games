from games.CurrencyRoulette import CurrencyRoulette
from games.GuessGame import GuessGame
from games.MemoryGame import MemoryGame
from utilities.Live import Setup, load_game
from utilities.Utils import get_scores, add_scores

game = Setup()
score_initial = get_scores(game.name)
score = 0
game.welcome(score_initial)

game_choice = load_game()

while game_choice != 'end':
    match game_choice:
        case "1":
            score = score + MemoryGame(game.name).play()
        case "2":
            score = score + GuessGame(game.name).play()
        case "3":
            score = score + CurrencyRoulette(game.name).play()
        case _:
            print("This is not a valid option. Please choose an option between 1 and 3. ")
    game_choice = load_game()

game.goodbye(score, score_initial)
add_scores(game.name, score_initial, score)
