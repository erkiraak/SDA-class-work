import datetime
import time
from contextlib import contextmanager
import timeit


def process_timer_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        _result = func(*args, **kwargs)
        end_time = time.time()
        return f'{func.__name__} took {end_time - start_time} seconds'

    return wrapper


@contextmanager
def process_timer():
    start = datetime.datetime.now()
    yield
    stop = datetime.datetime.now()
    difference = stop - start
    print(f'contextmanager took {difference} seconds')


def minimum_from_list(list):
    if not list:
        return None
    minimum = list[0]
    for element in list:
        if element < minimum:
            minimum = element
    return minimum


@process_timer_function
def minimum_from_list_with_wrapper(list):
    return minimum_from_list(list)


def combine(list):
    result = []
    for x in list:
        for y in list[::-1]:
            result.append((x, y))
    return result


@process_timer_function
def combine_with_decorator(list):
    return combine(list)


if __name__ == "__main__":
    for item in [1_000_000, 10_000_000, 100_000_000]:
        with process_timer():
            minimum_from_list(range(item, 0, -1))
        minimum_from_list_with_wrapper(range(item, 0, -1))
        print(f"timeit took {timeit.timeit(lambda: minimum_from_list(range(item, 0, -1)), number=1)} seconds")

    print("")

    for item in [100, 1_000, 10_000]:
        with process_timer():
            combine(range(item))
        combine_with_decorator(range(item))
        print(f"timeit took {timeit.timeit(lambda: combine(range(item)), number=1)} seconds")
