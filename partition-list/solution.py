# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        rootBeforeX = beforeX = ListNode(0)
        rootAfterX = afterX  = ListNode(0)

        while(head):
            hNext = head.next
            if (head.val < x):
                beforeX.next = head
                beforeX = beforeX.next
            else:
                afterX.next = head
                afterX = afterX.next
            head = head.next
        afterX.next = None
        beforeX.next = rootAfterX.next

        return rootBeforeX.next
