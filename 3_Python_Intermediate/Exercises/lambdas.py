words = ["assa", "a", "ab", "cd", "cc"]

palindromes = list(filter(lambda w: w == w[::-1], words))

print(palindromes)
