# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if p2 == None:
                return False
            p2 = p2.next
            if p1 == p2:
                return True
        return False
