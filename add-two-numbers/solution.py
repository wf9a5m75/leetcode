# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        ans = root
        carryUp = 0

        # 9->9
        # 9->9->9
        # ------------
        #

        while(A and B):
            aNext = A.next
            A.next = None
            root.next = A

            s = A.val + B.val + carryUp
            A.val = s % 10
            carryUp = s // 10

            A = aNext
            B = B.next

            if (root.next):
                root = root.next

        remain = A if A else B
        if remain:
            while(remain):
                remainNext = remain.next
                root.next = remain
                remain.next = None

                s = remain.val + carryUp
                remain.val = s % 10
                carryUp = s // 10

                remain = remainNext

                if (root.next):
                    root = root.next
        if carryUp > 0:
            c = ListNode(carryUp)
            root.next = c

        return ans.next
