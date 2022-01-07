class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        pre = [0] * N
        tail = [0] * N

        pre[0] = nums[0]
        tail[N - 1] = nums[N - 1]
        for i in range(1, N):
            pre[i] = max(nums[i], nums[i] + pre[i - 1])
            tail[N - i - 1] = max(nums[N - i - 1], nums[N - i - 1] + tail[N - i])


        def helper(L: int, R: int) -> int:
            if (L == R):
                return nums[L]
            mid = (L + R) >> 1
            return max(helper(L, mid), helper(mid + 1, R), pre[mid] + tail[mid + 1])
        return helper(0, N - 1)
