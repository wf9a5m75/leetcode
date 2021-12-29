class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        #
        # Summation approach
        #
        N = len(nums)
        if (N < 3):
            return 0

        R = 2
        ans = 0
        while(R < N):
            L = R
            while(R < N) and (nums[R - 2] - nums[R - 1] == nums[R - 1] - nums[R]):
                R += 1
            cnt = (R - L)
            ans += (cnt * (cnt + 1)) >> 1
            R += 1

        return ans
