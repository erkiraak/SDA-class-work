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


if __name__ == "__main__":
    results = []
    for list_of_numbers in [[random.randint(1, 1000) for _ in range(random.randint(5, 10))] for _ in range(5)]:
        results.append(sum_product(list_of_numbers))
        print(results[-1])

    sum_product([1, 3, "a"])
    sum_product(1)
    sum_product([])
    print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]))


