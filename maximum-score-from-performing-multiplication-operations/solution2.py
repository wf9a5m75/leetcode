class Solution:
    def maximumScore_backtrack(self, nums: List[int], multipliers: List[int]) -> int:
        M = len(multipliers)
        N = len(nums)

        @cache
        def dp(i: int, L: int) -> int:
            # Can't move ahead anymore
            if i == M:
                return 0

            #        [0, 1, 2, 3]
            # i = 0   L        R ( = N -1 - L)
            #
            # i = 1      L     R ( = N - 1 - i + L)
            # i = 1   L     R ( = N - 1 - i + L)
            #
            R = N - 1 - i + L

            multi = multipliers[i]

            return max(multi * nums[L] + dp(i + 1, L + 1),
                       multi * nums[R] + dp(i + 1, L))
        return dp(0, 0)

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        M = len(multipliers)
        N = len(nums)

        dp = [[0] * (M + 1) for _ in range(M + 1)]
        for i in range(M - 1, -1, -1):
            multi = multipliers[i]
            for L in range(i, -1, -1):
                R = N - 1 - i + L
                dp[i][L] = max(multi * nums[L] + dp[i + 1][L + 1],
                                multi * nums[R] + dp[i + 1][L])
        return dp[0][0]
