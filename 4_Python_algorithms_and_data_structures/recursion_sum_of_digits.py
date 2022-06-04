def sum_of_digits(n: int):
    return sum([int(digit) for digit in str(n)])


def sum_of_digits_recursive(n: int):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits_recursive(n // 10)


print(sum_of_digits(21))
print(sum_of_digits_recursive(21399))


def quad_2(num):
    count = 0
    for i in range(num):
        for j in range(num):
            count += 1

    return f"loop ran {count} times"


def quad_3(num):
    count = 0
    for i in range(num):
        for j in range(num):
            for k in range(num):
                count += 1

    return f"loop ran {count} times"


print(quad_2(25))
print(quad_3(250))
