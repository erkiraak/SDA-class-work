from singleton_decorator import Singleton
from game_factory import GameFactory


@Singleton
class GameMaster:
    def __init__(self):
        self.credit = 100

    def host_game(self, game_type):
        game = GameFactory.create_object(game_type)
        self.credit += game.play_game()


    def __str__(self):
        return f"Game Master capital: {self.credit}"



if __name__ == "__main__":
    gm = GameMaster()
    gm.host_game("sum")