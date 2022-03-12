def max_of_two(a, b):
    return a if a > b else b


def max_of_three(a, b, c):
    return max_of_two(max_of_two(a, b), c)


max_of_two_lambda = lambda a, b: a if a > b else b

max_of_three_lambda = lambda a, b, c: max_of_two_lambda(max_of_two_lambda(a, b), c)

print(max_of_two(1, 3))
print(max_of_three(1, 5, 3))
print(max_of_two_lambda(1, 3))
print(max_of_three_lambda(1, 5, 3))

list_of_int = [1, 2, 3, 4, 5]


def return_odd(int_list):
    return [item for item in int_list if item % 2 == 1]


def return_even(int_list):
    return [item for item in int_list if item % 2 == 1]


return_odd_lambda = list(filter(lambda a: a % 2, list_of_int))
return_even_lambda = list(filter(lambda a: a % 2 == 0, list_of_int))

print(return_odd(list_of_int))
print(return_even(list_of_int))
print(return_odd_lambda)
print(return_even_lambda)
