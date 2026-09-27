def find_closest_lt_target(low, high, arr, target):
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] < target:
            low = mid+1;
        else:
            high = mid-1;
    return low


def two_Sum_lt_k(arr, k):
    # a+b < k
    # a - k < -b
    # k - a > b
    # So basically try to find max value of b such that (a+b) < k
    
    arr = sorted(arr)
    ans = -1
    n = len(arr)
    for i in range(n-1):
        to_find = k - arr[i]
        ind = find_closest_lt_target(i+1, n-1, arr, to_find)
        if ind == i:
            continue
        ans = max(ans, arr[i]+arr[ind])
    return ans

if __name__ == "__main__":
    arr = [1, 4, 8, 10, 6, 3]
    k = 19
    # ans = two_Sum_lt_k(arr, k)
    # print(ans)
    with open('two_sum_less_than_k_test_cases.txt', 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 5):
            arr = eval(lines[i])
            k = eval(lines[i+1])
            expected = eval(lines[i+2])
            ans = two_Sum_lt_k(arr, k)
            assert expected == ans