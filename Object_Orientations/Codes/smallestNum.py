import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.current = 1
        self.added_back = set()
        self.min_heap = []

    def popSmallest(self) -> int:
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)
            self.added_back.remove(smallest)
            return smallest
        
        smallest = self.current
        self.current += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_back:
            heapq.heappush(self.min_heap, num)
            self.added_back.add(num)

obj = SmallestInfiniteSet()

while True:
    print("\nChoose an operation:")
    print("1: popSmallest()")
    print("2: addBack(num)")
    print("3: Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        result = obj.popSmallest()
        print(f"Smallest popped: {result}")
    elif choice == '2':
        num = int(input("Enter number to add back: "))
        obj.addBack(num)
        print(f"{num} added back to the set.")
    elif choice == '3':
        break
    else:
        print("Invalid input. Try again.")
