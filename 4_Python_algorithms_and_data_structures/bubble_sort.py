def bubble_sort(arr):
    swap_count = 0
    swapped = True
    position = len(arr)
    while swapped:
        swapped = False
        for i in range(1, position):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
                swap_count +=1
        position -= 1
    print(swap_count)
    return arr


print(bubble_sort([44, 23423, 32, 231, 1232, 121, 1212, 5, 1, 3242, 32, 1, 1251, 1, 35334, 7, 3, 12]))
print(bubble_sort([44, 32, 1232, 121, 1212, 5, 1, 3242, 32, 1, 1251, 1, 35334, 7, 3, 12]))
print(bubble_sort([1, 1, 1, 3, 5, 7, 12, 32, 32, 44, 121, 231, 1212, 1232, 1251, 3242, 23423, 35334]))
