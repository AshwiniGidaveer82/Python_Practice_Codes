class Solution:
    def generate(self, numRows: int):
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)  
            
         
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            triangle.append(row)

        return triangle


sol = Solution()
print(sol.generate(5))  # Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
print(sol.generate(1))  # Output: [[1]]
