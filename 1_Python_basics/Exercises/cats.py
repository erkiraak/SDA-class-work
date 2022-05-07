def cat_checker(amount):
    if amount < 0 or not isinstance(amount, int):
        return "Incorrect number of cats"
    elif amount == 1:
        return "Alice has 1 cat"
    else:
        return f"Alice has {amount} cats"

print(cat_checker(-2))
