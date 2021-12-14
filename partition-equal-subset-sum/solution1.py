class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        DP
            time complecity: O(N * half)
            space complecity: O(N * half)
        """
        total = sum(nums)
        if total & 1 == 1:
            return False

        half = int(total / 2)
        N = len(nums)
        dp = [[False] * (half + 1) for _ in range(N + 1)]
        dp[0][0] = True

        # Try all numbers one by one
        for i, num in enumerate(nums):
            for m in range(half):
                dp[i + 1][m] |= dp[i][m]

                if m + num <= half:
                    dp[i + 1][m + num] |= dp[i][m]

        return dp[N][int(half)]
