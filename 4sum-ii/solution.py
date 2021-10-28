from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        # O(N * N)
        mem = defaultdict(int)
        for c in nums3:
            for d in nums4:
                mem[c + d] += 1


        # O(N * N)
        results = 0
        for a in nums1:
            for b in nums2:
                r = 0 - a - b
                if (r in mem):
                    results += mem[r]
        return results
