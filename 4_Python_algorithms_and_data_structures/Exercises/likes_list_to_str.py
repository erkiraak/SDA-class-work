from typing import List


def likes(names: List[str]) -> str:
    if len(names) == 0:
        return "No one likes this"
    if len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) > 3:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"


print(likes([])) # => "nobody likes it"
print(likes(["Peter"])) # => "Peter likes it!"
print(likes(["Peter", "Anna"])) # => "Peter and Anna like it"
print(likes(["Peter", "Anna", "Mark"])) # => "Peter, Anna and Mark like it"
print(likes(["Peter", "Anna", "Mark", "Ola"])) # => "Peter, Anna and 2 other people like it"
print(likes(["Peter", "Anna", "Mark", "Ola", "Jenny"])) # => "Peter, Anna and 3 other people like it"