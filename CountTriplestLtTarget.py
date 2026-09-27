from functools import lru_cache
from typing import List
    
class Solution:    
        
    def threeSum(self, nums: List[int], target) -> int:        
        nums = sorted(nums)        
        n = len(nums)        
        ans = 0        
        for i in range(n-1):            
            if i > 0 and nums[i] == nums[i-1]:                
                continue            
            t = target - nums[i]            
            j, k = i+1, n-1            
            while j < k:                
                if nums[j] + nums[k] < t:                    
                    ans += 1
                    j += 1
                    while j+1 < k and nums[j] == nums[j+1]:
                        j += 1
                elif nums[j] + nums[k] >= t:                    
                    k -= 1        
        return ans
    
sol = Solution()
print(sol.threeSum([0, 0, 0, ,2], 3))