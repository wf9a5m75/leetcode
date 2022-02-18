# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return None
        rest = None
        if (head.next):
            rest = self.swapPairs(head.next.next)
            head, tail = head.next, head

            head.next = tail
            tail.next = rest

        return head
        
