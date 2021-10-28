# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddRoot = ListNode(0)
        evenRoot = ListNode(0)
        heads = [evenRoot, oddRoot]

        isEven = True
        while(head):
            headNext = head.next
            head.next = None
            heads[int(isEven)].next = head
            heads[int(isEven)] = head

            isEven = not isEven
            head = headNext

        # heads[1] is located at the tail of odd linked list
        heads[1].next = evenRoot.next
        return oddRoot.next
