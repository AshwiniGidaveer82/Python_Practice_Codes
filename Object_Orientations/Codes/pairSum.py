from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Convert linked list to array
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next

        # Step 2: Calculate maximum twin sum
        max_sum = 0
        n = len(values)
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            max_sum = max(max_sum, twin_sum)

        return max_sum

# Helper function to create linked list from list
def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Test the code
input_list = [5, 4, 2, 1]
head = create_linked_list(input_list)

sol = Solution()
print("Output:", sol.pairSum(head))  # Expected Output: 6
