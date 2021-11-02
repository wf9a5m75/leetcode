# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head):
        n = 0
        while(head):
            head = head.next
            n += 1

        return n

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head

        n = self.getLength(head)
        if n == 0:
            return head
        p = n - (k % n)
        if p == n:
            return head

        left = ListNode(0)
        pLeft = left
        last = head
        while(head) and (p > 0):

            pNext = head.next

            pLeft.next = head
            pLeft = pLeft.next

            last = head
            head = head.next
            p -= 1

        pLeft.next = None

        right = head
        while(head):
            last = head
            head = head.next
        last.next = left.next


        return right

        
