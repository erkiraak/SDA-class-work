class EvenNumber():
    def __init__(self, maximum):
        self.max = maximum
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number > self.max:
            raise StopIteration
        elif not self.number % 2:
            return self.number
        return self.__next__()


class Squares():
    def __init__(self, maximum):
        self.max = maximum
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        if self.number > self.max:
            raise StopIteration
        else:
            return self.number ** 2


def even_number(maximum):
    number = 0
    while number < maximum:
        number += 1
        if not number % 2:
            yield number
        else:
            even_number(maximum)


def squares(maximum):
    number = 0
    while number < maximum:
        number += 1
        yield number ** 2


for i in EvenNumber(2):
    print(i)

for i in even_number(2):
    print(i)

for i in Squares(2):
    print(i)

for i in squares(2):
    print(i)
