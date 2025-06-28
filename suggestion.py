from typing import List
import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()  # Sort lexicographically
        res = []
        prefix = ""

        for c in searchWord:
            prefix += c
            # Find the first index where product starts with prefix
            i = bisect.bisect_left(products, prefix)
            suggestions = []
            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
            res.append(suggestions)
        
        return res
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
