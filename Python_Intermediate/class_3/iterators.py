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


def range_generator(from_, to_, step):
    number = from_
    if not step:
        raise ValueError("Step cannot be 0")

    if step < 0:
        if from_ < to_:
            raise ValueError("In case of negative step, from_ has to be higher than to_")
        while number > to_:
            yield number
            number += step
    else:
        while number < to_:
            yield number
            number += step


for number in range_generator(8, 1, -2):
    print(number)

# for i in EvenNumber(2):
#     print(i)
#
# for i in even_number(2):
#     print(i)
#
# for i in Squares(2):
#     print(i)
#
# for i in squares(2):
#     print(i)
