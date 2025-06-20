from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / mid)

            if total_hours <= h:
                right = mid
            else:
                left = mid + 1

        return left

# ---------- INPUT HANDLING -------------
# Take input from user
piles_input = input()  # e.g., 3 6 7 11
piles = list(map(int, piles_input.strip().split()))

h = int(input("Enter number of hours: "))  # e.g., 8

# ---------- CALL FUNCTION -------------
solution = Solution()
result = solution.minEatingSpeed(piles, h)
print("Minimum eating speed Koko needs:", result)
