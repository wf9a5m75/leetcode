class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        #
        # DP
        #  Time : O(N * N)
        #  Space : O(N)
        #
        N = len(nums)
        if (N < 2):
            return N

        up = [0] * N
        down = [0] * N

        for i in range(1, N):
            for j in range(i):
                if (nums[j] > nums[i]):
                    down[i] = max(down[i], up[j] + 1)
                elif (nums[j] < nums[i]):
                    up[i] = max(up[i], down[j] + 1)
        return 1 + max(up[N - 1], down[N - 1])
