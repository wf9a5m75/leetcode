class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mem = {}
        for i, val in enumerate(nums):
            if (val in mem) and (i - mem[val] <= k):
                return True
            mem[val] = i
        return False
