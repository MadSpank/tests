# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
 
#     return i + 1

# def quicksort(arr, low, high):

#     if low < high:
#         pi = partition(arr, low, high)
#         quicksort(arr, low, pi - 1)
#         quicksort(arr, pi + 1, high)

# data = [1,2,6,1,2,4, -3]

# print('Unsorted array', end='\n')
# print(data)
# quicksort(data, 0, len(data) - 1)
# print('Sorted array', end='\n')

# print(data)


def divide_and_conquer(arr):
    if len(arr) == 3 or len(arr) == 4:
        if arr[0] < arr[-1]:
            return arr[0: len(arr) // 2], arr[len(arr) // 2:]
        else:
            return arr
    

def mergesort(arr):

    if arr[0] < arr[-1]:
        divide_and_conquer(arr)