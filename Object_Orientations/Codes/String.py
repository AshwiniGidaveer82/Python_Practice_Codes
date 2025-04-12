class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for char in s:
            # Check if the last two characters are same as the current one
            if len(result) < 2 or not (result[-1] == result[-2] == char):
                result.append(char)
        return ''.join(result)


sol = Solution()
print(sol.makeFancyString("leeetcode"))  # Output: "leetcode"
print(sol.makeFancyString("aaabaaaa"))   # Output: "aabaa"
print(sol.makeFancyString("aab"))        # Output: "aab"
