class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)

        increase = [0] * N
        decrease = [0] * N

        ans = 0
        for i in range(1, N):
            for j in range(i):
                if nums[j] < nums[i]:
                    increase[i] = max(increase[i], decrease[j] + 1)
                elif nums[j] > nums[i]:
                    decrease[i] = max(decrease[i], increase[j] + 1)
        return max(increase[N - 1], decrease[N - 1]) + 1
