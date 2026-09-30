def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        idx = i
        for j in range(i-1, -1, -1):
            if key <= arr[j]:
                arr[j+1] = arr[j]
                idx = j
            else:
                break
        arr[idx] = key
    
# [3,4,1,7,2,5] --> i=1, j-(0)
# [3,4,1,7,2,5] --> i=2, j-(1,0) --> [1,3,4,7,2,5]
# [1,3,4,7,2,5] --> i=3, j-(2,0) --> [1,3,4,7,2,5]
# [1,3,4,7,2,5] --> i=4, j-(3,0) --> [1,2,3,4,7,5]
# [1,2,3,4,7,5] --> i=5, j-(4,0) --> [1,2,3,4,5,7]

arr = [3,4,1,7,2,5] 
insertion_sort(arr)
print(arr)

arr = [3,4,1,7,2,5,11,9,1,0,12,54,21,45,21,43,23,65,34,76,52,17] 
insertion_sort(arr)
print(arr)


    
