import random
import timeit
from sort_bubble import bubble_sort


def merge_sort1(input_list):
    return_list = []
    if len(input_list) >= 2:
        mid_list = len(input_list) // 2
        list1 = merge_sort1(input_list[:mid_list])
        list2 = merge_sort1(input_list[mid_list:])
        while list1 or list2:
            if not list1:
                return_list.append(list2.pop(0))
            elif not list2:
                return_list.append(list1.pop(0))
            elif list1[0] < list2[0]:
                return_list.append(list1.pop(0))
            else:
                return_list.append(list2.pop(0))
    else:
        return_list = input_list
    return return_list

def merge_sort2(input_list):
    return_list = []
    if len(input_list) >= 2:
        mid_list = len(input_list) // 2
        list1 = merge_sort2(input_list[:mid_list])
        list2 = merge_sort2(input_list[mid_list:])
        while list1 and list2:
            if list1[0] < list2[0]:
                return_list.append(list1.pop(0))
            else:
                return_list.append(list2.pop(0))
        return_list.extend(list1)
        return_list.extend(list2)
    else:
        return_list = input_list
    return return_list


input_list = [random.randint(0, 100000) for _ in range(100000)]

# print(timeit.timeit(lambda: bubble_sort(input_list), number=10))
print(timeit.timeit(lambda: merge_sort1(input_list), number=100))
print(timeit.timeit(lambda: merge_sort2(input_list), number=100))
