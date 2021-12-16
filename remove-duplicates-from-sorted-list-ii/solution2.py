# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return head
        anchor = ListNode(0)
        root = anchor
        p1 = head
        p2 = head.next
        while(p2):
            if (p1.val != p2.val):
                root.next = p1
                root = root.next
                p1 = p1.next
                p2 = p2.next
            else:
                while(p2) and (p1.val == p2.val):
                    p2 = p2.next
                p1 = p2
                if (p2):
                    p2 = p2.next

        root.next = p1
        return anchor.next
