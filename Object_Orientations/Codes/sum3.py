from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int], target: int):
            if len(path) == k:
                if target == 0:
                    result.append(path[:])
                return

            for i in range(start, 10): 
                if i > target:
                    break
                path.append(i)
                backtrack(i + 1, path, target - i)
                path.pop()

        backtrack(1, [], n)
        return result

# --------------------------------------
# 🧪 Input + Execution Code
# --------------------------------------
if __name__ == "__main__":
    k = int(input())
    n = int(input())

    sol = Solution()
    combinations = sol.combinationSum3(k, n)
    print("Valid combinations are:", combinations)
