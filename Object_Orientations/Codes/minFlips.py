class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a > 0 or b > 0 or c > 0:
            abit = a & 1
            bbit = b & 1
            cbit = c & 1

            if (abit | bbit) != cbit:
                if cbit == 1:
                    
                    flips += 1
                else:
                   
                    flips += abit + bbit

            a >>= 1
            b >>= 1
            c >>= 1

        return flips
sol = Solution()
print(sol.minFlips(2, 6, 5))  # Output: 3
