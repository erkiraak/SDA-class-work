from math import sqrt


def quadratic_zero_check(a, b, c):
    if a == 0:
        print("a cannot be 0")
        return
    elif b ** 2 - 4 * a * c < 0:
        print("imaginary numbers not calculated")
        return
    elif b ** 2 - 4 * a * c == 0:
        x1 = -b / (2 * a)
        return x1
    else:
        x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return x1, x2


print(quadratic_zero_check(5, 2, 1))
