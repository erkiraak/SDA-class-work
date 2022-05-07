from singleton_decorator import Singleton
import random


@Singleton
class Dice:
    def __init__(self):
        self.number_of_rolls = 0
        self.record = {}
        self.last_roll = 0
        for i in range(1, 7):
            self.record[str(i)] = 0, 0.00

    # complete this method
    def roll(self):
        roll = str(random.randint(1, 6))
        self.last_roll = int(roll)
        self.number_of_rolls += 1
        for record in self.record:
            if record == roll:
                self.record[record] = self.record[record][0] + 1, round(((self.record[record][0] + 1) / self.number_of_rolls), 2)
            else:
                self.record[record] = self.record[record][0], round((self.record[record][0] / self.number_of_rolls), 2)

        return int(roll)

    def __str__(self):
        return str(self.record)


if __name__ == "__main__":
    dice = Dice()
    for _ in range(10000):
        dice.roll()
    print(dice)
    print(dice.number_of_rolls)
