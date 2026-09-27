
def sort(arr):
    n = len(arr)
    for i in range(n):
        min_ = arr[i]
        idx = i
        for j in range(i+1, n):
            if min_ > arr[j]:
                min_ = arr[j]
                idx = j
        arr[i], arr[idx] = min_, arr[i]
    return arr

a = [5,2,3,1,4]
print(sort(a))        