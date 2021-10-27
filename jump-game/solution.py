
from typing import List
class Solution:

    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        if (N == 1):
            return True

        last_pos = N - 1
        for i in range(N - 1, -1, -1):
            if (i + nums[i] >= last_pos):
                last_pos = i
        return last_pos == 0


    def canJump_slow(self, nums: List[int]) -> bool:
        N = len(nums)
        if (N == 1):
            return True

        dp = [False] * N
        dp[0] = True

        for r, num in enumerate(nums):
            if (dp[N - 1]):
                break
            if (dp[r]):
                for y in range(1, num + 1):
                    dp[min(N - 1, r + y)] = True
        # print(dp)
        return dp[N - 1]
