def factorial(number):
    result = 1
    if number < 2:
        return result
    while number >= 2:
        result *= number
        number -= 1
    return result


print(factorial(5))


def fact(number):
    if number < 2:
        return 1
    while number >= 2:
        return number * fact(number - 1)




print(fact(5))
