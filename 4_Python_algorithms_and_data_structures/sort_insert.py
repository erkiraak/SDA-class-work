def insertion_sort(arr, reverse=False):
    swap_count = 0
    if not reverse:
        for i in range(1, len(arr)):
            while i > 0:
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    swap_count += 1
                else:
                    break
                i -= 1
    else:
        for i in range(1, len(arr)):
            while i > 0:
                if arr[i] > arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    swap_count += 1
                else:
                    break
                i -= 1
    print(swap_count)
    return arr


print(insertion_sort([44, 23423, 32]))
print(insertion_sort([44, 23423, 32, 231, 1232, 121, 1212, 5, 1, 3242, 32, 1, 1251, 1, 35334, 7, 3, 12]))
print(insertion_sort([44, 23423, 32, 231, 1232, 121, 1212, 5, 1, 3242, 32, 1, 1251, 1, 35334, 7, 3, 12], reverse=True))
print(insertion_sort(
    insertion_sort([44, 23423, 32, 231, 1232, 121, 1212, 5, 1, 3242, 32, 1, 1251, 1, 35334, 7, 3, 12], reverse=True)))
