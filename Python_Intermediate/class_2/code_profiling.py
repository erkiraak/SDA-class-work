from timeit import timeit


def even_list_for():
    return [num for num in range(0, 1001) if not num % 2]


def even_list_while():
    number = 0
    even_number_list = []
    while number < 1001:
        if not number % 2:
            even_number_list.append(number)
        number += 1
    return even_number_list


def power():
    return [pow(n, 5) for n in range(1, 1001)]


setup = """from math import pow"""

print(timeit(stmt=even_list_for, number=1000))
print(timeit(stmt=even_list_while, number=1000))
print(timeit(stmt=power, setup=setup, number=1000))
print(even_list_for())