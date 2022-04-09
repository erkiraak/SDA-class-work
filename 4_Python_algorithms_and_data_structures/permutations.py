from timeit import timeit
from functools import cache

@cache
def permutations(string: str):
    list_of_permutations = []
    if len(string) == 1:
        return [string]
    else:
        for index, letter in enumerate(string):
            for permutation_return in permutations(string[:index] + string[index + 1:]):
                if (permutation_final := letter + permutation_return) not in list_of_permutations:
                    list_of_permutations.append(permutation_final)
    return list_of_permutations


print(timeit(stmt=lambda: permutations("12345678"), number=100, setup="from timeit import timeit\nfrom functools import cache"))