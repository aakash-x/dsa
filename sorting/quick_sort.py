def partition(start, end, arr):
    pivot = arr[end]
    right = end - 1
    left = start

    while left <= right:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    arr[right + 1], arr[end] = arr[end], arr[right + 1]
    return right + 1

# def partition(start, end, arr):
#     pivot = arr[end]
#     boundary = start - 1

#     for current in range(start, end):
#         if arr[current] <= pivot:
#             boundary += 1
#             arr[boundary], arr[current] = arr[current], arr[boundary]

#     pivot_index = boundary + 1
#     arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
#     return pivot_index    
    

def quick_sort(start, end, arr):
    if start < end:
        partition_ind = partition(start, end, arr)
        quick_sort(start, partition_ind-1, arr)
        quick_sort(partition_ind+1, end, arr)

arr = [4, 1, 3, 5]
quick_sort(0, len(arr)-1, arr)
print(arr)

arr = [4, 1, 3, 5,9,11,4,5,7,2]
quick_sort(0, len(arr)-1, arr)
print(arr)    

arr = [1,0]
quick_sort(0, len(arr)-1, arr)
print(arr)    

arr = [9,5,6,7,1]
quick_sort(0, len(arr)-1, arr)
print(arr)    