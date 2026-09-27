def merge(start, mid, end, arr):
    # merges two sorted arrays
    #  0. 1. 2. 3
    # [1, 4, 3, 5] ------> [1, 4] and [3, 5]
    # start = 0, end = 3, mid = 1
    n1 = mid - start + 1 # +1 required, check above eg
    n2 = end - mid 
    tmp = [None] * (n1+n2)
    t = 0
    i, j = start, mid+1
    while i <= mid and j <= end:
        if arr[i] > arr[j]:
            tmp[t] = arr[j]
            j += 1
            t += 1
        else:
            tmp[t] = arr[i]
            i += 1
            t += 1
    while i <= mid:
        tmp[t] = arr[i]
        i += 1
        t += 1
    while j <= end:
        tmp[t] = arr[j]
        j += 1
        t += 1      
    
    arr[start: end+1] = tmp

def mergeSort(start, end, arr):
    mid = (end + start) // 2
    if start < end:
        mergeSort(start, mid, arr)
        mergeSort(mid+1, end, arr)
        merge(start, mid, end, arr)
        

# [4, 1, 3, 5] , start = 0, end = 3, 0 <= 3 
# -- mid --> 1, mS(0, 1), ms(2, 3), mid(0, 1, 3)
# mS(0, 1) :: mid --> 0, mS(0, 0), mS(1,1), mid(0, 0, 1)
# mid(0, 0, 1) :: [4, 1] --> [4] [1] --> [1, 4]
# ms(2, 3) :: mid --> 2, mS(2, 2), mS(3,3), mid(2, 2, 3)
# mid(2, 2, 3) :: [3, 5] --> [3] [5] --> [3, 5]
# mid(0, 1, 3) :: [1, 4, 3, 5] --> n1=2, n2=2 [1, 4] & [3, 5] --> [1, 3, 4, 5]

arr = [4, 1, 3, 5]
mergeSort(0, len(arr)-1, arr)
print(arr)

arr = [4, 1, 3, 5,9,11,4,5,7,2]
mergeSort(0, len(arr)-1, arr)
print(arr)


                 