from typing import List
class Solution:

    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        if (N == 1):
            return True

        # We try to move from N - 1 to 0
        last_pos = N - 1
        for i in range(N - 1, -1, -1):

            if (i + nums[i] >= last_pos):
                last_pos = i
        
        return last_pos == 0
