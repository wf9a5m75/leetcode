# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return None

        faster = slower = head

        while(True):
            faster = faster.next
            if (faster == None):
                return None
            faster = faster.next
            if (faster == None):
                return None
            slower = slower.next
            if (faster == slower):
                break

        p1 = head
        p2 = slower
        while(p1 != p2):
            p1 = p1.next
            p2 = p2.next
        return p1
