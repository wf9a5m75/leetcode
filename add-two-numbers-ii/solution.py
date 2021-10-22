# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:

        stackA, stackB = [], []
        ptrA, ptrB = A, B
        while(ptrA or ptrB):
            if ptrA:
                stackA.append(ptrA.val)
                ptrA = ptrA.next
            if ptrB:
                stackB.append(ptrB.val)
                ptrB = ptrB.next

        C = A if len(stackA) > len(stackB) else B

        root = None
        carryUp = 0
        while(stackA and stackB):
            cNext = C.next
            C.next = root

            s = stackA.pop() + stackB.pop() + carryUp
            C.val = s % 10
            carryUp = s // 10
            root = C

            C = cNext

        remain = stackA if stackA else stackB
        while(remain):
            cNext = C.next
            C.next = root

            s = remain.pop() + carryUp
            C.val = s % 10
            carryUp = s // 10
            root = C

            C = cNext

        if carryUp > 0:
            newDigit = ListNode(carryUp)
            newDigit.next = root
            root = newDigit
        return root


            
