
n = [1, 3, 5]
N = len(n)

ans = []
for mask in range(1<<N):
    sum = []
    for i in range(N):
        if mask & (1<<i):
            sum.append(n[i])
    ans.append(sum)
        
print(ans)