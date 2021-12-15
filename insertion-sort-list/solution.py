# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-5001)

        r = result
        while(head):
            target = head
            head = head.next
            target.next = None

            # If the last tail of the r is smaller than the target,
            # just keep continuing.
            # Otherwise, search from the top.
            if r.val > target.val:
                r = result
            while(r.next) and (r.next.val < target.val):
                r = r.next

            # insert the target
            rNext = r.next
            r.next = target
            target.next = rNext

            r = r.next

        return result.next
