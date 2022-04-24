import heapq


def heap_sort(lst):
    heapq.heapify(lst)
    sorted_list = []
    while True:
        try:
            sorted_list.append(heapq.heappop(lst))
        except IndexError:
            break
    return sorted_list


print(heap_sort([3, 7, 3, 2, 12, 321, 13, 865, 34, 1, 121]))