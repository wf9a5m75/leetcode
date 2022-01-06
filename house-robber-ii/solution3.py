class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if (N == 1):
            return nums[0]
        if (N == 2):
            return max(nums[0], nums[1])
        robs0 = [0] * N
        robs1 = robs0.copy()

        robs0[0] = nums[0]
        robs0[1] = max(robs0[0], nums[1])

        robs1[1] = nums[1]
        robs1[2] = max(robs1[1], nums[2])

        for i in range(2, N):
            robs0[i] = max(robs0[i - 2] + nums[i], robs0[i - 1])
            robs1[i] = max(robs1[i - 2] + nums[i], robs1[i - 1])
        return max(robs0[N - 2], robs1[N - 1])
