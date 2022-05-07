# def count_vowels(string):
#     count = 0
#     for letter in string.lower():
#         if letter in "aeiouy":
#             count += 1
#     return count
#
#
# print(count_vowels("Write a function (or program) that will determine the number of vowels in a given string."))

from collections import Counter


def count_vowels(string):
    count = 0
    counter = Counter(string.lower())
    for symbol, amount in counter.items():
        if symbol in "aeiouy":
            count += amount
    return count


print(count_vowels("Write a function (or program) that will determine the number of vowels in a given string."))
