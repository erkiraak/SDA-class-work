from random import randint


def do_not_repeat():
    numbers = set()
    for _ in range(10):
        number = randint(0, 10)
        if number in numbers:
            print("Oh no! I repeated myself!")
        numbers.add(number)
    return numbers


output = do_not_repeat()
print(output)
print(type(output))