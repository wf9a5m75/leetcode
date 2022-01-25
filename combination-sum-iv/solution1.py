class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0] * (target + 1)
        dp[0] = 1

        for rest in range(target + 1):
            for num in nums:
                if rest - num >= 0:
                    dp[rest] += dp[rest - num]
        return dp[target]
