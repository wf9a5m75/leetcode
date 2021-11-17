class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [0] * N
        dpL = dpR = 0
        j = N - 2
        for i in range(1, N):
            dpL += (nums[i] - nums[i - 1]) * i
            dpR += (nums[j + 1] - nums[j]) * i
            ans[i] += dpL
            ans[j] += dpR
            j -= 1
        return ans
