from collections import Counter

class Solution:
    def commonChars(self, words):
        common_count = Counter(words[0])
        for word in words[1:]:
            common_count &= Counter(word) 
        return list(common_count.elements())

sol = Solution()
print(sol.commonChars(["bella","label","roller"]))  # Output: ["e","l","l"]
print(sol.commonChars(["cool","lock","cook"]))      # Output: ["c","o"]
