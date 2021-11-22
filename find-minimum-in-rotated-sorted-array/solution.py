class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        L = 0
        R = N - 1
        while(L != R):
            mid = (L + R) >> 1
            if (nums[L] < nums[R]):
                return nums[L]
            if (nums[mid] > nums[R]):
                L = mid + 1
            else:
                R = mid
        return nums[L]
