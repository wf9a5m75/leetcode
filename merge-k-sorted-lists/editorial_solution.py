# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Approach 5: Merge with Divide and Conquer
    #
    # We don't need to traverse most nodes many times repeatedly
    #
    # (1) Pair up k lists and merge each pair
    #
    # (2) After the first pairing, k lists are merged into k/2 lists
    #     with average 2N / k length, then k/4, k/8 and so on.
    #
    # (3) Repeat this procedure until we get the final sorted linked list
    #
    # Thus, we'll traverse almost N nodes pairing and merging, and repeat this procedure
    # about log2(k) times.
    #
    # ---------------------
    # Time complexity: O(N log k) where k is the number of linked lists.
    #
    #    We can merge two sorted linked list in O(n) time where n is
    #    the total number of nodes in two lists.
    #
    #    Sum up the merge process and we can get: O(Σ 1→log2(k) N) = O(N log k)
    #
    # Space complexity: O(1)
    #    We don't use any extra space.
    #
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, A: List[Optional[ListNode]], B: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = point = ListNode(0)
        while(A and B):
            if A.val <= B.val:
                point.next = A
                A = A.next
            else:
                point.next = B
                B = B.next
            point = point.next
        if A is None:
            point.next = B
        else:
            point.next = A
        return head.next
