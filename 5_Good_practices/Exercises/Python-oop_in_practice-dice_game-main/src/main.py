from gamemaster import GameMaster
from dice import Dice

if __name__ == "__main__":
    gm = GameMaster()
    p = int(input("How many parity games de you want to play? "))
    s = int(input("How many sum games do you want to play? "))
    for i in range(p):
        gm.host_game("parity")
    for j in range(s):
        gm.host_game("sum")

    print(gm)
    print(Dice())
