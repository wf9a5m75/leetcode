class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #
        # Greedy
        #   O(N) times
        #   O(1) spaces
        #
        N = len(nums)
        ans = currS = nums[0]
        for i in range(1, N):
            currS = max(currS + nums[i], nums[i])
            ans = max(ans, currS)
        return ans
