# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = p1 = p2 = head

        n = 1
        while(p != None):
            if (n < k):
                p1 = p1.next
            p = p.next
            n += 1

        i = 1
        while(i < n - k):
            p2 = p2.next
            i += 1

        p1.val, p2.val = p2.val, p1.val
        return head



    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = p1 = p2 = head
        for i in range(k - 1):
            p = p.next
        p1 = p

        while(p.next != None):
            p = p.next
            p2 = p2.next

        p1.val, p2.val = p2.val, p1.val
        return head
