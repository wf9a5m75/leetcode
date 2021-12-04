# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        fast = slow = head
        while(fast.next):
            fast = fast.next
            if fast.next:
                fast = fast.next
            slow = slow.next

        while(slow):
            sNext = slow.next
            slow.next = None
            stack.append(slow)
            slow = sNext

        while(head):
            hNext = head.next
            if hNext != stack[-1]:
                head.next = stack.pop()
                head.next.next = hNext
                head = hNext
            else:
                break
            
