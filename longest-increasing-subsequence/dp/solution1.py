class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        ans = 1
        for i in range(1, N):
            for j in range(i):
                if (nums[j] < nums[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        # print(dp)
        return ans
