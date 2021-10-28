# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Floyd's algorithm
        # https://leetcode.com/problems/find-the-duplicate-number/solution/
        if head == None:
            return None
        p1 = head
        p2 = head

        while(True):
            p1 = p1.next
            p2 = p2.next

            # p2 moves twice nodes faster than p1.
            # That's why p2 would be reached to the end if exists.
            if (p2 == None):
                return None
            p2 = p2.next
            if (p2 == None):
                return None

            if p1 == p2:
                break

        # P2 would catch p1 in somewhere.
        # It should be the same distance to the entrance of the cycle
        # from the head and the p2 position
        p1 = head
        while (p1 != p2):
            p1 = p1.next
            p2 = p2.next

        return p1
