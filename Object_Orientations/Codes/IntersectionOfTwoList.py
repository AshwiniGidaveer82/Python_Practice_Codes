class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    pA, pB = headA, headB
    
    while pA != pB:
        pA = pA.next if pA else headB  
        pB = pB.next if pB else headA  

    return pA  




common = ListNode(8, ListNode(10))

headA = ListNode(4, ListNode(1, common))


headB = ListNode(5, ListNode(6, ListNode(1, common)))


result = getIntersectionNode(headA, headB)
print(result.val if result else "No Intersection")  # Output: 8
