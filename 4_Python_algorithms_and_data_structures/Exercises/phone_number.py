from typing import List


def create_phone_number(n: List[int]) -> str:
    # return f"(+{''.join(map(str, n[:2]))}) {''.join(map(str, n[2:5]))}-{''.join(map(str, n[5:8]))}-{''.join(map(str, n[8:]))}"
    return "(+{}{}) {}{}{}-{}{}{}-{}{}{}".format(*n)
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]))

