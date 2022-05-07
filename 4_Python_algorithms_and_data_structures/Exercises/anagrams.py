from typing import List


def anagrams(word: str, lst_of_words: List[str]) -> List[str]:
    """
    Given a word and a list of words, return a list of all the words that are anagrams of the given word.
    """
    return [w for w in lst_of_words if sorted(w) == sorted(word)]

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer']))
print(anagrams('laser', ['lazing', 'lazy',  'lacer', 'laser']))