from dataclasses import dataclass, field, InitVar
from typing import List

@dataclass
class Test:
    first_int: InitVar[int]
    multiplier: InitVar[int]
    list_of_ints: InitVar[List[int]]
    second_int: InitVar[int] = field(default=0)
    calculated_val: float = field(init=False)

    def __call__(self, *args, **kwargs):
        return self.calculated_val

    def __post_init__(self, first_int: int, multiplier: int, list_of_ints: list[int], second_int: int):
        self.calculated_val = first_int * multiplier * sum(list_of_ints) - second_int


t = Test(first_int=3, multiplier=3, list_of_ints=[2, 2], second_int=9)
print(t)
print(t())
print(t() * 2)
