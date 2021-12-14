from test import checkTests
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        backtracking
            time complecity: O(N)
                Since we stop traversing if s > half, so O(N / 2).
                But we also try both cases, s+nums[i] and s.
                It means O(2 * (N / 2)) = O(N)

            space complecity: O(N)
                We use DB memoization. Since we stop traversing at half point,
                but we try two cases. Thus, O(2 * (N / 2)) = O(N)
        """

        N = len(nums)
        total = sum(nums)
        half = total / 2

        mem = {}
        def walker(i, s):
            if (s > half) or (i == N):
                return False
            if (s + nums[i] == half):
                return True

            key = "{}:{}".format(i, s)
            if (key in mem):
                return mem[key]

            mem[key] = walker(i + 1, s + nums[i]) or walker(i + 1, s)
            return mem[key]
        return walker(0, 0)

def wrap(nums: List[int]) -> bool:
    return Solution().canPartition(nums)

checkTests(wrap)
