from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        
        count = 0  
        end = float('-inf') 

        for interval in intervals:
            if interval[0] < end:
               
                count += 1
            else:
               
                end = interval[1]
        
        return count
sol = Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))  # Output: 1
