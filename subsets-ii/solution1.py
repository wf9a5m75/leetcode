import heapq
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        dp = [ [] ]
        nums.sort()
        prev = None
        for num in nums:
            if prev == num:
                start = end
            else:
                start = 0
            end = len(dp)
            # print(start, end, nums[start: end])
            for i in range(start, end):
                dp += [dp[i] + [num]]
            prev = num
            # print("------")
        return dp
