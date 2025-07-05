from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n == 0:
            return 0

        dp0 = 0
        dp1 = -prices[0]

        for i in range(1, n):
            temp = dp0
            dp0 = max(dp0, dp1 + prices[i] - fee)  
            dp1 = max(dp1, temp - prices[i])      

        return dp0
sol = Solution()
print(sol.maxProfit([1, 3, 2, 8, 4, 9], 2))  # Output: 8
