from math import sqrt


def previous_prime_checker(number):
    checked_number = number - 1
    if checked_number == 2:
        return True
    elif checked_number % 2 == 0 or checked_number == 1:
        return False

    for n in range(3, int(sqrt(checked_number)) + 1, 2):
        if not checked_number % n:
            return False
    return True


for i in range(1, 101):
    print(previous_prime_checker(i), i - 1)
