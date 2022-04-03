import timeit
from recursion_with_timer_decorator import process_timer_function, process_timer

def print_pairs(list):
    if list:
        for i in list:
            for j in list:
                for k in list:
                    for l in list:
                        print(i, j, k, l)

@process_timer_function
def print_pairs_with_decorator(list):
    if list:
        for i in list:
            for j in list:
                for k in list:
                    for l in list:
                        print(i, j, k, l)

if __name__ == "__main__":
    for list in [range(1, 13)]:
        decorator_result = print_pairs_with_decorator(list)
        timeit_result = f"timeit took {timeit.timeit(lambda: print_pairs(list), number=1)} seconds"
        with process_timer() as t:
            print_pairs(list)

    print(decorator_result)
    print(timeit_result)
