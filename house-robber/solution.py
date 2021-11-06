class Solution:
    def rob(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]
        if (len(nums) == 2):
            return max(nums[0], nums[1])

        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N):
            # Pick the higher total amount from two cases:
            #  1) robbing the house at i - 2
            #          -> we can rob the house at i
            #
            #  2) or robbing the house i - 1
            #          -> we can Not rob the house at i,
            #             because the house i - 1 has security system
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[N - 1]
        
