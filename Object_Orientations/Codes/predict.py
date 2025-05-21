from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant_queue = deque()
        dire_queue = deque()
        
        # Step 1: Populate the queues with the indices of 'R' and 'D'
        for i, s in enumerate(senate):
            if s == 'R':
                radiant_queue.append(i)
            else:
                dire_queue.append(i)
        
       
        while radiant_queue and dire_queue:
            r_index = radiant_queue.popleft()
            d_index = dire_queue.popleft()
            
            
            if r_index < d_index:
                radiant_queue.append(r_index + n) 
            else:
                dire_queue.append(d_index + n)  
        
       
        return "Radiant" if radiant_queue else "Dire"
solution = Solution()
print(solution.predictPartyVictory("RD"))    # Output: "Radiant"
print(solution.predictPartyVictory("RDD"))   # Output: "Dire"
