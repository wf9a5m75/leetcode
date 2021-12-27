class Solution:
    def rob(self, nums: List[int]) -> int:

        N = len(nums)
        if (N == 1):
            return nums[0]
        if (N == 2):
            return max(nums[0], nums[1])

        dp = [0] * N

        # Assuming we rob at index 0
        dp[0] = nums[0]

        # If we choose dp[0], it means we start from 0, then skip at index 1.
        # If we choose nums[1], it means we start from 1 (we didn't rob at index 0)
        dp[1] = max(dp[0], nums[1])

        for i in range(2, N):
            # In order to rob at index i, we must be located at i-2 before.
            # Otherwise, we skip the house at index i.
            # Records the maximum amount.
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[N - 1]
