
# a = [1, 2 ,4]
# b = [4, 8 ,9]
# d = 1

# a = [4, 2, 1] : m
# b = [9, 8, 4, 2, 1, 0] : n
# d = 1


# # mlogm + nlogn + m+n

# a = [1, 10 , 5, 8 , 3]
# b = [9 , 11, 6, 2, 7]
# d = 3

# a = [10, 8, 5, 3, 1]
#                i          
# # b = [5, 6, 7, 9, 11]
# b = [17, 15, 13, 12,12,12, 9, 7, 6, 5]
# d = 1

# abs(a[i] - b[j]) <= d
# -(a[i]-b[j]) < 0
# b[j] - a[i] <= d
# b[j] <= a[i] +d

# (a[i]-b[j]) <= d, X
# a[i] <= b[j] + d
# a[i] - d <= b[j]


# b[j] <= a[i] + d
# a[i] - d <= b[j]

# a[i] - d <= b[j] <= a[i] + d



def lower_bound(arr, key, low, high):
    """_summary_

    Args:
        low (int): lower boundry
        high (int): upper boundry
        arr (List[int]): sorted in desc order
        key (int): item to search

    Returns:
        int: right most closest index to `key`
    """
    mid = low + (high - low)//2
    if low <= high:
        if arr[mid] >= key:
            return lower_bound(arr, key, mid+1, high)
        else:
            return lower_bound(arr, key, low, mid-1)
    return mid

def right_most_upper_bound(low, high, arr, target):
    mid = low + (high-low)//2
    if low <= high:
        if arr[mid] >= target:
            low = mid+1;
        else:
            high = mid-1;
    return mid
    

def solver(arr1, arr2, d):
    arr1.sort(reverse=True)
    arr2.sort(reverse=True)
    
    ans = 0
    i = 0
    left, right = 0, len(arr2)-1
    m, n = len(arr1), len(arr2)
    while i < m:
        j = lower_bound(arr2, arr1[i], left, right)
        if j < 0: 
            j = 0
        if (j == n-1 and abs(arr2[j]-arr1[i] > d)):
            ans += 1
            left = j
        elif abs(arr2[j]-arr1[i]) > d and abs(arr2[j+1]-arr1[i]) > d:
            ans += 1
            left = j
        i += 1
    return ans
        
    

        
if __name__ == "__main__":
    # a1 = [10,8,8,6,5,4,2,2,2,1]
    # print(len(a1))
    # print(lower_bound(a1, 0, 0, len(a1)-1))

    arr1 = [7,9,4]
    arr2 = [-10]
    d = 29
    print(solver(arr1, arr2, d))
    
    arr1 = [2,1,100,3]
    arr2 = [-5,-2,10,-3,7]
    d = 6
    print(solver(arr1, arr2, d))    