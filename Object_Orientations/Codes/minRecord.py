from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        
        for u, v in connections:
            graph[u].append((v, True))  
            graph[v].append((u, False)) 

        visited = [False] * n
        self.changes = 0

        def dfs(node):
            visited[node] = True
            for neighbor, is_original in graph[node]:
                if not visited[neighbor]:
                    if is_original:
                        self.changes += 1
                    dfs(neighbor)

        dfs(0)
        return self.changes
