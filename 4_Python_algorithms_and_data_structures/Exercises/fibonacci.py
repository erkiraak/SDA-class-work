# from timeit import timeit
# from functools import lru_cache
#
#
# def fibonacci(nth):
#     a = 0
#     b = 1
#     for i in range(nth):
#         a, b = b, a + b
#     return a
#
#
# # print(fibonacci(50))
#
# @lru_cache(maxsize=10)
# def fibonacci_recursive(nth):
#     if nth < 1:
#         return 0
#     elif nth < 2:
#         return 1
#     return fibonacci_recursive(nth - 1) + fibonacci_recursive(nth - 2)

# print(fibonacci_recursive(20))
#
# print(timeit(stmt=lambda: fibonacci(110), number=10))
# print(timeit(stmt=lambda: fibonacci_recursive(150), number=10))
# print(fibonacci_recursive.cache_info())


def gcd(a, b):
    while a != b and a != 0 and b != 0:
        if a > b:
            a, b = a - b, b
        else:
            a, b = a, b - a
    if a == 0 or b == 0:
        return "Not found"
    elif a == b:
        return a


print(gcd(8, 12))
