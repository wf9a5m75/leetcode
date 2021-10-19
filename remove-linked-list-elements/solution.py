# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        root = ListNode(0)
        ans = root
        while head:
            if head.val != val:
                root.next = head
                root = head
            head = head.next
        if (root):
            root.next = None
        return ans.next
