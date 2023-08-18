def buble_sort(arr):

    for i in range(len(arr)):
        for j in range(1,len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr



arr = [1,4,2,5,10,3]
print(buble_sort(arr))