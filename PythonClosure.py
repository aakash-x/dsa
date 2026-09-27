from collections import defaultdict
def converter(id, mem = dict(), cache=defaultdict(int)):
    res = cache.get(id)
    print(cache)
    if res:
        print("found in cache")
        return res
    if id in mem:
        print("not found in cache")
        cache[id] = mem[id]
        return cache[id]
    else:
        cache[id] = id
        return id
    
mem = {2:4, 5: 25, 4: 16, 6: 36}

res = converter(2, mem) 
res = converter(2, mem) 
res = converter(3, mem) 
res = converter(4, mem) 
res = converter(8)
res = converter(8, mem)
res = converter(2) 
res = converter(2, cache=dict()) 
res = converter(4, mem)
    