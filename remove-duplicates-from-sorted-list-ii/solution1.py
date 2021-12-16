# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(-101)
        initAnchor = root

        path = [root]
        while(head):
            if root.val != head.val:
                path.append(head)
                root.next = head
                root = root.next
                head = head.next
            else:
                while(head) and (root.val == head.val):
                    head = head.next
                path.pop()
                root = path[-1]
                root.next = head

        root.next = None
        return initAnchor.next
