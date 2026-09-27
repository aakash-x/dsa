from typing import List
from threading import Lock



def bubbleSort(arr: List[int]):
    for i in range(len(arr)):
        swap = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break
    # return arr
    
    # i = 0, 1
    # j = 0, 1, 
    #     2,5,3 
    
    
    # 0,1,  2,3, 3,4 
    
import threading

inp = [5,2,3,1,4,6,9,7,8]


# // odd even transform - sort
                 
    
bubbleSort(inp)
print(inp)