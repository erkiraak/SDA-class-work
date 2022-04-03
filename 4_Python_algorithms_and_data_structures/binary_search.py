def bin_search(arr, target):
    start = 0
    stop = len(arr) - 1
    while start <= stop:
        mid = (stop + start) // 2
        if arr[mid] == target:
            return f"Key found at index {mid} in array"
        else:
            if arr[mid] < target:
                start = mid + 1
            else:
                stop = mid - 1
    return f"Key not found in array"


def bin_search_with_recursion(arr, target, start=0, stop=None):
    start = start
    if stop is None:
        stop = len(arr) - 1
    else:
        stop = stop

    mid = (stop + start) // 2
    if arr[mid] == target:
        return f"Key found at index {mid} in array"
    if start <= stop:
        if arr[mid] < target:
            start = mid + 1
            return bin_search_with_recursion(arr, target, start, stop)
        else:
            stop = mid - 1
            return bin_search_with_recursion(arr, target, start, stop)
    return f"Key not found in array"


print(bin_search_with_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))
