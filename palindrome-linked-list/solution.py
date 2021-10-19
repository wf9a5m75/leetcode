# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return True

        # Find the half point
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        # Change the reverse order from the half point
        reverse = None
        while(slow):
            sNext = slow.next
            slow.next = reverse
            reverse = slow
            slow = sNext

        # Then compair each node
        while(reverse):
            if (head.val != reverse.val):
                return False
            head = head.next
            reverse = reverse.next

        return True
        
