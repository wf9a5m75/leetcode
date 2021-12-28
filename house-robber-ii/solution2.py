class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if (N == 1):
            return nums[0]
        if (N == 2):
            return max(nums[0], nums[1])

        rob0 = [0] * N
        rob1 = [0] * N

        # Case1 : start from index 0
        rob0[0] = rob0[1] = nums[0]

        # Case2 : start from index 1
        rob1[1] = nums[1]

        # Calculate the maximum amounts
        for i in range(2, N):
            rob0[i] = max(rob0[i - 2] + nums[i], rob0[i - 1])
            rob1[i] = max(rob1[i - 2] + nums[i], rob1[i - 1])

        # The case1 takes the range from 0 to N - 2,
        # and the case2 takes the range from 1 to N - 1.
        return max(rob0[N - 2], rob1[N - 1])
