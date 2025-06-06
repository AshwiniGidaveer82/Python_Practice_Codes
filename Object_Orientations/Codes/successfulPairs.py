from bisect import bisect_left
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()  # Sort potions for binary search
        n = len(potions)
        result = []

        for spell in spells:
            # Minimum required potion strength for this spell
            required = success / spell

            # Find the first potion >= required
            index = bisect_left(potions, required)
            result.append(n - index)  # Count of successful potions

        return result

