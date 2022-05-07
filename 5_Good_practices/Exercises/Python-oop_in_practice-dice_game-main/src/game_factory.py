from game import ParityGame, SumGame


class GameFactory:
    @staticmethod
    def create_object(game_type):
        if game_type.lower() == "parity":
            return ParityGame()
        elif game_type.lower() == "sum":
            return SumGame()
        else:
            print("Incorrect game type")

if __name__ == "__main__":
    game1 = GameFactory.create_object("sum")
    print(type(game1))
    game2 = GameFactory.create_object("parity")
    print(type(game2))
