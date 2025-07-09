class StockSpanner:
    
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1  
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
# Initialize
obj = StockSpanner()

# Calls
print(obj.next(100))  # Output: 1
print(obj.next(70))   # Output: 2
print(obj.next(75))   # Output: 4
print(obj.next(85))   # Output: 6
