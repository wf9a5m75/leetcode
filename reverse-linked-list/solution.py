# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def iterator_solution(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = None
        while head:
            headNext = head.next

            head.next = root
            root = head

            head = headNext
        return root

    def recursive_solution(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head.next):
            root, ans = self.recursive_solution(head.next)
            head.next = None
            root.next = head
            root = root.next

            return root, ans
        else:
            return head, head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.iterator_solution(head)

        if (not head):
            return head
        root, ans = self.recursive_solution(head)
        return ans
