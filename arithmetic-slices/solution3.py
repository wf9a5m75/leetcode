class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        ans = 0
        for i in range(2, N):
            if nums[i - 2] - nums[i - 1] == nums[i - 1] - nums[i]:
                dp[i] = dp[i - 1] + 1
                ans += dp[i]
        return ans
