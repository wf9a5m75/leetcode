# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:

        root = ListNode(0)
        top = root
        while(A is not None) and (B is not None):
            aNext = A.next
            bNext = B.next
            if A.val < B.val:
                root.next = A
                A = aNext
            else:
                root.next = B
                B = bNext
            root = root.next

        rest = None
        if A is not None:
            rest = A
        elif B is not None:
            rest = B
        root.next = rest
        return top.next
            
