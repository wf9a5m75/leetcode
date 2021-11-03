# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        root = prev
        root.next = head
        while(head):
            n1 = head
            n2 = head.next
            if n2:
                n2Next = n2.next
                prev.next = n2
                n2.next = n1
                n1.next = n2Next
                prev = n1
                head = n2Next
            else:
                head = None
        return root.next
                
