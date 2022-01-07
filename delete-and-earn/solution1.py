class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        N = max(nums)
        dp = [0] * (N + 1)
        for num in nums:
            dp[num] += num

        prev = curr = 0
        for i in range(N + 1):
            prev, curr = curr, max(curr, prev + dp[i])
        return curr
