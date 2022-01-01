class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        # dp[i] denotes the maximum Length Of Subseq possible for characters from index {i} if i included
        dp = [1]*size  # LIS

        for i in range(size-2, -1, -1):
            # we can take one by one combination with sub-indexes
            for j in range(i+1, size):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
