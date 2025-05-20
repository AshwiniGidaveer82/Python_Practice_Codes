class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    stack.pop()

                elif stack[-1] == -ast:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(ast)

        return stack
sol = Solution()

print(sol.asteroidCollision([5, 10, -5]))   # Output: [5, 10]
print(sol.asteroidCollision([8, -8]))       # Output: []
print(sol.asteroidCollision([10, 2, -5]))   # Output: [10]
