import heapq
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #
        # DP approach
        #   Time complexity: O(N * 2 ** N)
        #   Space complexity: O(N * 2 ** N)
        #
        # (init) [[]]
        #
        # nums[0] = 1
        #   start = 0, end = 1
        #   [] + [1] => add [1]
        #
        #   (after) dp = [[], [1]]
        #
        # nums[1] = 2
        #   start = 0, end = 2
        #   [] + [2]  => add [2]
        #   [1] + [2] => add [1, 2]
        #
        #   (after) dp = [[], [1], [1, 2]]
        #
        # nums[2] = 2
        #   start = 2, end = 2
        #   [1, 2] + [2]  => add [1, 2, 2]
        #
        #   (after) dp = [[], [1], [1, 2], [1, 2, 2]]
        #
        # nums[3] = 3
        #   start = 0, end = 3
        #   [] + [3]  => add [3]
        #   [1] + [3]  => add [1, 3]
        #   [1, 2] + [3]  => add [1, 2, 3]
        #   [1, 2, 2] + [3]  => add [1, 2, 2, 3]
        #
        #   (after) dp = [[], [1], [1, 2], [1, 2, 2], [3], [1, 3], [1, 2, 3], [1, 2, 2, 3]]


        dp = [ [] ]
        nums.sort()
        prev = None
        for num in nums:
            if prev == num:
                start = end
            else:
                start = 0
            end = len(dp)
            # print(start, end, nums[start: end], dp[start])
            for i in range(start, end):
                dp += [dp[i] + [num]]
            prev = num
            # print(dp)
            # print("------")
        return dp
