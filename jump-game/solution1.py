
from typing import List
class Solution:

    def canJump_slow(self, nums: List[int]) -> bool:
        N = len(nums)
        if (N == 1):
            return True

        dp = [False] * N
        dp[0] = True

        # Flagging boolean takes O(N * N)
        for r, num in enumerate(nums):
            if (dp[N - 1]):
                break
            if (dp[r]):
                for y in range(1, num + 1):
                    dp[min(N - 1, r + y)] = True
        # print(dp)
        return dp[N - 1]
