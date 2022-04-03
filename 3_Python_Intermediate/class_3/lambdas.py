from functools import reduce
import random

list_of_int = [random.randint(0, 30) for x in range(30)]


def max_of_two(a, b):
    return a if a > b else b


def max_of_three(a, b, c):
    return max_of_two(max_of_two(a, b), c)


max_of_two_lambda = lambda a, b: a if a > b else b

max_of_three_lambda = lambda a, b, c: max_of_two_lambda(max_of_two_lambda(a, b), c)

max_of_three_lambda_if_nest = lambda a, b, c: a if (a > b and a > c) else (b if (b > a and b > c) else c)

print(max_of_three_lambda_if_nest(92, 612, 9))


def max_of_n_reduce(*args): return reduce(lambda a, b: a if a > b else b, [*args])


max_of_list_reduce = reduce(lambda a, b: a if a > b else b, list_of_int)


# print(max_of_list_reduce)
# print(max_of_n_reduce(1, 4, 6, 234, 32))
# print(max_of_two(1, 3))
# print(max_of_three(1, 5, 3))
# print(max_of_two_lambda(1, 3))
# print(max_of_three_lambda(1, 5, 3))


def return_odd(int_list):
    return [item for item in int_list if item % 2 == 1]


def return_even(int_list):
    return [item for item in int_list if item % 2 == 0]


list_odd_comprehension = [x for x in list_of_int if (lambda x: x % 2 == 1)]

list_odd_filter = list(filter(lambda a: a % 2, list_of_int))
list_even_filter = list(filter(lambda a: a % 2 == 0, list_of_int))

greater_than = list(filter(lambda x: x > 15, list_of_int))
is_it_greater = list(map(lambda x: x > 15, list_of_int))

sum_of_squares = reduce(lambda x, y: x + y, map(lambda x: x ** 2, list_of_int))

print(sum_of_squares)
# print(list(zip(list_of_int, is_it_greater)))
# print(greater_than)
# print(return_odd(list_of_int))
# print(return_even(list_of_int))
# print(list_odd_comprehension)
# print(list_odd_filter)
# print(list_even_filter)

animals = ["cat", "dogs", "monkey"]

length_of_values_map = dict(map(lambda a: (a, len(a)), animals))

length_of_values_dict_comprehension = {animal: len(animal) for animal in animals}


# print(length_of_values_map)
# print(length_of_values_dict_comprehension)

class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

    def __repr__(self):
        return f"{self.make} {self.model} {self.price}"

    def __lt__(self, other):
        return self.price < other.price


cars = [
    Car("Ford", "Anglia", 300.0),
    Car("Ford", "Cortina", 700.0),
    Car("Alfa Romeo", "Stradale 33", 190.0),
    Car("Alfa Romeo", "Giulia", 500.0),
    Car("Citroën", "2CV", 75.0),
    Car("Citroën", "Dyane", 105.0),
    Car("Bmw", "Coupe", 1200.0),
    Car("Bmw", "i-series", 2500.0),
    Car("Ford", "puma", 1750),
    Car("Ford", "focus", 4200),
    Car("Jeep", "Compass", 2350),
    Car("Jeep", "Cheroke", 7200),
]

cheap_cars = list(filter(lambda x: x.price < 120, cars))
expensive_cars = list(filter(lambda x: x.price > 300, cars))
cheapest_ford = reduce(lambda x, y: x if x.price < y.price else y, filter(lambda x: x.make == "Ford", cars))
most_expensive = reduce(lambda x, y: x if x.price > y.price else y, cars)
ford_total_price = reduce(lambda x, y: x + y, map(lambda x: x.price, filter(lambda x: x.make == "Ford", cars)))
number_of_jeeps = len(list(filter(lambda x: x.make == "Jeep", cars)))
number_of_fords = reduce(lambda x, y: 2 if isinstance(x, Car) else x + 1, filter(lambda x: x.make == "Ford", cars))

print(cheap_cars)
print(expensive_cars)
print(cheapest_ford)
print(most_expensive)
print(f"Total for all Fords: {ford_total_price}")
print(f"Total number of Jeeps: {number_of_jeeps}")
print(f"Total number of Jeeps: {number_of_fords}")

sorted_cars = sorted(cars, key=lambda x: x.price, reverse=True)

print(sorted_cars)

sorted_cars2 = sorted(cars)
print(sorted_cars2)