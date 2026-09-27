from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        # Base case: Amount = 0 can be made with 1 way (by not choosing any coin)
        for i in range(n):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for amt in range(1, amount + 1):
                # Not take the current coin
                not_take = dp[i + 1][amt]
                
                # Take the current coin if it's <= amt
                take = 0
                if coins[i] <= amt:
                    take = dp[i][amt - coins[i]]

                dp[i][amt] = take + not_take

        return dp[0][amount]


Solution().change(5, [1, 2, 5])  # Example usage