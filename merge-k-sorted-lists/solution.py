# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #
        # Store all values of all lists into a hash table,
        # then rebuild a List
        #
        # Time complexity is O(NK + klogk + k) ≒ O(NK)
        # Space complexity is O(NK)

        #
        # (1) Store all values of all lists into a hash table
        #
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

        #
        # (2) Sort kinds
        #
        kinds = list(mem)
        kinds.sort()

        #
        # (3) Connects each list
        #
        root = ListNode(0)
        ans = root
        for val in kinds:
            root.next = mem[val]["head"]
            root = mem[val]["tail"]
        return ans.next
