class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #
        # DP approach
        #   O(N) times
        #   O(N) spaces
        #
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        ans = dp[0]
        for i in range(N - 1):
            dp[i + 1] = max(dp[i] + nums[i + 1], nums[i + 1])
            ans = max(ans, dp[i + 1])
        return ans
