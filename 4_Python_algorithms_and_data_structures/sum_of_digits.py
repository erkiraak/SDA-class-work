def sum_of_digits(n: int):
    return sum([int(x) for x in str(n)])

def sum_of_digits_recursive(n: int):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits_recursive(n // 10)

print(sum_of_digits(21))
print(sum_of_digits_recursive(21399))
