class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        lowest = nums[0]
        N = len(nums)
        for i in range(1, N):
            if nums[i] < lowest:
                lowest = nums[i]
            elif nums[i] > lowest:
                ans = max(ans, nums[i] - lowest)
        return ans
