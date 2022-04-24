def recursive_sum(integer: int):
    try:
        if integer < 0:
            raise ValueError
        if integer <= 1:
            return integer
        else:
            return integer + recursive_sum(integer - 1)
    except TypeError:
        return "Only integers allowed"
    except ValueError:
        return "Only positive integers allowed"

print(recursive_sum("a"))
print(recursive_sum(-2))
print(recursive_sum(100))

