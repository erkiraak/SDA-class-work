"""
1 We split a given list into two halves
     we split both halves into quarters
       ...
          we get two list with single elements
          we merge them element by element, starting with the smaller ones
       We merge the sorted list, getting a small sorted list
       ...
2. We merge the two sorted halves, getting a sorted list.
"""
import random

"""
Given a list of two sorted array - merge the two sorted array into 1 array.
We will assume that the list has been divided into two.
e.g 
[5, 10, 20, 29] [15, 18, 22, 30] 
"""


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    list_left = lst[:mid]
    list_right = lst[mid:]
    return merge_two_lists(merge_sort(list_left), merge_sort(list_right))


def merge_two_lists(list_left, list_right):
    sorted_list = []
    len_left = len(list_left)
    len_right = len(list_right)
    left_i = right_i = 0
    while left_i < len_left and right_i < len_right:
        if list_left[left_i] < list_right[right_i]:
            sorted_list.append(list_left[left_i])
            left_i += 1
        else:
            sorted_list.append(list_right[right_i])
            right_i += 1
    while left_i < len_left:
        sorted_list.append(list_left[left_i])
        left_i += 1
    while right_i < len_right:
        sorted_list.append(list_right[right_i])
        right_i += 1
    return sorted_list


# lst = [5, 10, 20, 29, 15, 18, 4, 30, 1]
for i in range(5, 20):
    int_lst = [random.randint(0, 100) for _ in range(i)]
    result = merge_sort(int_lst)
    print(f"Sorted list: {result}")
