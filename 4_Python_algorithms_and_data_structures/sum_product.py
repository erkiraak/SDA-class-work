from functools import reduce
import random


def sum_product(list):
    try:
        return {
            'list': list,
            'sum': sum(list),
            'product': reduce(lambda x, y: x * y, list)
        }
    except TypeError:
        print("A non-empty list with only numbers is required")



results = []
for list_of_numbers in [[random.randint(1, 1000) for _ in range(random.randint(5, 10))] for _ in range(5)]:
    results.append(sum_product(list_of_numbers))
    print(results[-1])

sum_product([1, 3, "a"])
sum_product(1)
sum_product([])
