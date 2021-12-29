class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        #
        # count up approach
        #
        N = len(nums)
        ans = 0
        cnt = 0
        for i in range(2, N):
            if (nums[i - 2] - nums[i - 1] == nums[i - 1] - nums[i]):
                cnt += 1
                ans += cnt
            else:
                cnt = 0

        return ans
