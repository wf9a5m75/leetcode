# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        length = 0
        while(fast.next and fast.next.next):
            slow = slow.next

            length += 2
            fast = fast.next.next

        if fast.next:
            length += 1

        n -= 1
        if n == length:
            return head.next

        root = head
        prev = None
        while(length != n):
            length -= 1
            prev = root
            root = root.next
        prev.next = root.next

        return head
            
