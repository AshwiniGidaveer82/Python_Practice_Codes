from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
sol = Solution()
print(sol.countBits(5))  # Output: [0, 1, 1, 2, 1, 2]
