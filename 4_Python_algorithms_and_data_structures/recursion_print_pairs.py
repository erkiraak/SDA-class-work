import timeit
from recursion_with_timer_decorator import process_timer_function, process_timer


def print_pairs(input_list):
    if input_list:
        for i in input_list:
            for j in input_list:
                for k in input_list:
                    for l in input_list:
                        print(i, j, k, l)


@process_timer_function
def print_pairs_with_decorator(input_list):
    if input_list:
        for i in input_list:
            for j in input_list:
                for k in input_list:
                    for l in input_list:
                        print(i, j, k, l)


if __name__ == "__main__":
    for int_list in [range(1, 13)]:
        decorator_result = print_pairs_with_decorator(int_list)
        timeit_result = f"timeit took {timeit.timeit(lambda: print_pairs(int_list), number=1)} seconds"
        with process_timer() as t:
            print_pairs(int_list)

    print(decorator_result)
    print(timeit_result)
