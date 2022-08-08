from games.BaseGames import BaseGames


class MemoryGame(BaseGames):

    def __init__(self, name, *super_params):
        self.name = name
        super().__init__(name, *super_params)

    def memory_game(self):
        self.load_game()
        print("Thank you for choosing to play the memory game. Unfortunately, Doron never gave me the second"
              "part of the project guidelines, so I don't know the requirements for this game. Please tell Doron to "
              "send me the second part of the project. Doron, if you are reading this, you know what to do ;-)")
        self.end_game()
