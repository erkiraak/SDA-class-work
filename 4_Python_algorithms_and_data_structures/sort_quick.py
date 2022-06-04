import random


def quick_sort(lst):
    if len(lst) < 2:
        return lst

    low_index = 0
    high_index = len(lst) - 1
    pivot_index = high_index
    # Make swaps while low and high have not met
    while low_index < high_index:
        if lst[low_index] > lst[pivot_index]:
            if lst[high_index] < lst[pivot_index]:
                lst[low_index], lst[high_index] = lst[high_index], lst[low_index]
            else:
                high_index -= 1
        else:
            low_index += 1
    # Swap pivot with index if needed
    if lst[low_index] > lst[pivot_index] and low_index < pivot_index:
        lst[low_index], lst[pivot_index] = lst[pivot_index], lst[low_index]
        pivot_index = low_index
    # Added this to avoid calls with empty lists
    if pivot_index == len(lst) - 1:
        return_list = quick_sort(lst[:pivot_index]) + [lst[pivot_index]]
    elif pivot_index == 0:
        return_list = [lst[pivot_index]] + quick_sort(lst[pivot_index + 1:])
    else:
        return_list = quick_sort(lst[:pivot_index]) + [lst[pivot_index]] + quick_sort(lst[pivot_index + 1:])

    return return_list


for _ in range(10):
    input_list = [random.randint(0, 199) for _ in range(10)]
    print(f"input list {input_list}")
    output_list = quick_sort(input_list)
    print(f"output list {output_list}")
