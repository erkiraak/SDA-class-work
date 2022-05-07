# Casino Games

In a casino, a game master offers two different games. Both games use only a single six sided dice and are described in the following.

## First Game - Sum Game
To play the first game, you pay 10 Euros. After the payment you proceed to throw the dice 4 times. The game master checks your throws:
* If you rolled a sum of 16 or 17 you get your payment of 10 Euros back.
* If you rolled an 18 or higher you receive 40 Euros.
* If you rolled less than 16, you receive nothing.

## Second Game - Parity Game
To play the second game, you also have to pay 10 Euros. Then you proceed to throw the dice three times. The game master counts the sum of your throws:
* if you get 3 pair numbers in all 3 throws, you win 50 euros.
* if you get an odd number in any throw, you receive nothing.

## Task 1
Implement a singleton decorator in the file ``src/singleton_decorator.py``. You will be using this decorator for other tasks down the line.

## Task 2
In the file ``src/die.py``, complete the class ``Die`` with the following functionalities:
* The class must be a singleton.

The dice record is a dictionary:
* The keys are numbers from 1 to 6.
* The respective values are tuples (numbers of occurrences of the number in the key, ratio of occurrences of the number in the key).


> For example; the die's record would be looking like this:
>
> {'1': (18, 0.14), '2': (28, 0.21), '3': (24, 0.18), '4': (17, 0.13), '5': (29, 0.21), '6': (21, 0.16)}
> 



Complete the method ``roll()`` of the class ``Dice``, so that:
* It randomly generates an integer between 1 and 6.
* It saves it as the last roll result of the dice.
* It counts the number of rolls so far.
* It updates the dice's record.
* It returns the number rolled.


## Task 3
In the file ``src/game.py``, complete the classes ``SumGame`` and ``ParityGame``:
* Implement the methods ``play_game()`` so that they respect the description of the games above.
* The method ``play_game()`` must return `self.gains` in both classes.

* Note that when a game is instantiated, gains are initialized to -10, which is the price for playing the game.
> Note: The gain that games represent, is the player's gain.


## Task 4
In the file ``src/game_facotry.py``, complete the method ``create_object(game_type)`` in the class ``GameFactory`` so that:
* When `game_type == parity`, it returns a ``ParityGame`` object.
* When `game_type == sum`, it returns a ``SumGame`` object.
* Do not forget to process invalid arguments.

## Task 5
In the file ``src/gamemaster.py``, complete the method ``host_game(game_type)`` in the class ``GameMaster`` so that:
* Depending on the type of the game chosen, a corresponding object is instantiated and the game is played.
* You use the factory method here.
* The game's gain are counted in the game-master's capital. Remember that a gain of a game is removed from the capital of the game-master.


> The method ``host_game(game_type)`` is an example of method overloading. The behaviour of the method depends on the type of its argument.

## Check your code
Run ``src/main.py`` to check if your code is acting as expected.

### Notes:

* The cashier (game-master) will always win, but the gains are not very large when divided by number of games.
* If you play a lot of games, all the ratios of the dice's record (singleton class) should convert to 0.17.

