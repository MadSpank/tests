def binary_search(arr, low, high, x):
    mid = (high + low) // 2

    if arr[mid] == x:
        return mid
    if x > mid:
        if x == high:
            return high
        binary_search(arr, mid + 1, high, x)

    else:
        if x == low:
            return low
        binary_search(arr, low, mid - 1, x)
    
    return -1


arr = [1,12,13, 15, 22, 26, 34, 37, 38, 50, 55]
x = 13

print(binary_search(arr,0, len(arr) -1,  x))