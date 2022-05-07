def to_weird_case(string: str) -> str:
    return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(string))

print(to_weird_case('This is a test'))