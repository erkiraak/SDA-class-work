
x = input("provide first number")
y = input("provide second number")

def add(a, b):
    try:
        a = float(a)
        b = float(b)
        return abs(a + b)
    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)

def divide(a, b):
    try:
        a = float(a)
        b = float(b)
        return a / b
    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)
    except ZeroDivisionError as error:
        print(error)



print(add(x, y))
print(divide(x, y))


