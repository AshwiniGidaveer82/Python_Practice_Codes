# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If there's only one node, return None
        if not head or not head.next:
            return None

        # Initialize slow and fast pointers
        slow = head
        fast = head
        prev = None

        # Move fast two steps and slow one step at a time
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Remove the middle node
        if prev:
            prev.next = slow.next

        return head
