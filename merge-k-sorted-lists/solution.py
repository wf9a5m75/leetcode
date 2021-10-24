# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mem = {}
        for L in lists:
            while(L):
                nextL = L.next
                L.next = None
                if L.val not in mem:
                    mem[L.val] = {
                        'head' : L,
                        'tail' : L
                    }
                else:
                    mem[L.val]["tail"].next = L
                    mem[L.val]["tail"] = L
                L = nextL

        kinds = list(mem)
        kinds.sort()

        root = ListNode(0)
        ans = root
        for val in kinds:
            root.next = mem[val]["head"]
            root = mem[val]["tail"]
        return ans.next
