class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N = len(nums)
        M = len(multipliers)

        dp = [[0] * (M + 1) for _ in range(M + 1)]

        for i in range(M - 1, -1, -1):
            multi = multipliers[i]

            for left in range(i, -1, -1):
                right = N - 1 - (i - left)
                dp[i][left] = max(dp[i + 1][left + 1] + multi * nums[left],
                                     dp[i + 1][left] + multi * nums[right])
        return dp[0][0]
