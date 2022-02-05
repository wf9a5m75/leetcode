# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #
        # Time complexity: O(N log k)  k ... the number of linked lists
        # Space complexity: O(N)
        #
        root = ListNode(0)
        curr = root
        hq = []
        for i, node in enumerate(lists):
            if (node):
                heapq.heappush(hq, (node.val, i))

        while(hq):
            val, listIdx = heapq.heappop(hq)
            node = lists[ listIdx ]
            curr.next = node
            curr = curr.next

            if (node.next):
                lists[listIdx] = lists[listIdx].next
                heapq.heappush(hq, (lists[listIdx].val, listIdx))

        curr.next = None

        return root.next
