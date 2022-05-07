from abc import ABC, abstractmethod
from dice import Dice


class Game(ABC):
    def __init__(self):
        self.gains = -10

    @abstractmethod
    def play_game(self):
        raise NotImplementedError()


class SumGame(Game):
    def play_game(self):
        dice = Dice()
        total = sum(dice.roll() for _ in range(4))
        if total >= 18:
            self.gains += 40
        elif total >= 16:
            self.gains += 10
        return self.gains


class ParityGame(Game):
    def play_game(self, number=3):
        dice = Dice()
        throws = [dice.roll() for _ in range(number)]
        for throw in throws:
            if throw % 2:
                return self.gains
        self.gains += 50
        return self.gains


if __name__ == "__main__":
    # game = SumGame()
    # for _ in range(10):
    #     print(game.play_game())
    counter_win = 0
    counter_lose = 0

    for _ in range(100):
        game = ParityGame()
        return_amount = game.play_game()
        if return_amount > 0:
            counter_win += 1
        else:
            counter_lose += 1

    print(f"wins: {counter_win}")
    print(f"losses: {counter_lose}")
