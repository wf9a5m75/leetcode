class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        # Greedy
        s = 0
        maxS = -10**4
        for num in nums:
            s = max(s + num, num)
            maxS = max(maxS, s)
        return maxS
