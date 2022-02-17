# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None) or (head.next == None):
            return head

        root = pp = ListNode(0)
        pp.next = head
        prev = head
        curr = prev.next
        while(curr != None):
            prev.next = curr.next
            curr.next = prev
            pp.next = curr

            pp = prev
            prev = prev.next
            if (prev):
                curr = prev.next
            else:
                curr = None
        return root.next
            
